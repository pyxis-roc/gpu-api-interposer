#!/usr/bin/env python3
#
# A simple parser for cuobjdump/nvdisasm output
#
# cuobjdump uses nvdisasm internally, and the right flags to nvdisasm
# can yield the assembly in the same format as cuobjdump.
#
# This was originally a line-based regexp parser, but broke for
# cuobjdump 10.2 output, and was converted to a simple recursive-descent
# parser.

import sys
import re
from collections import namedtuple

CUOBJDUMP_RE_FUNC_START = re.compile(r'\s+Function : (?P<function>[^\s]*)$')
CUOBJDUMP_RE_FUNC_END = re.compile(r'\s+\.+$')

SASS_INSN_CUOBJDUMP = namedtuple('SASS_INSN_CUOBJDUMP', 'loc opcode text raw vliw_start vliw_end')

# five forms: the first is the scheduling info, second is a standard opcode, third indicates start of vliw group, fourth indicates end of vliw group
#                                                                /* 0x001c4400e22007f6 */
#         /*0008*/                   MOV R1, c[0x0][0x20];       /* 0x4c98078000870001 */
#         /*00a8*/         {         MOV R4, c[0x0][0x148];      /* 0x4c98078005270004 */
#         /*00b0*/                   STG.E [R2], R0;        }    /* 0xeedc200000070200 */
# in 10.2, the opcode of the second VLIW instruction was shifted to the next line without a semicolon:
#         /*00b0*/                   STG.E [R2], R0        }
#                                                                /* 0xeedc200000070200 */

class ParseError(object):
    def error(self, tok, message):
        import sys
        print(f"{tok.err_scoord}: {message}", file=sys.stderr)
        print("    " + tok.err_line, file=sys.stderr)
        print(" "*(tok.err_coord[1][0]+4) +"^"*(tok.err_coord[1][1] - tok.err_coord[1][0]), file=sys.stderr)
        raise ValueError(message)

class DisassemblyTokenizer(object):
    token = None
    match = None
    _token_stream = None

    def __init__(self, strdata, err):
        self.data = strdata
        self._token_stream = self.tokenize()
        self.token, self.match = next(self._token_stream)
        self.err = err

    # convenience
    def error(self, message):
        self.err.error(self, message)

    def token_name(self, v):
        return self._tokens[v]

    def tokenize(self):
        # based on the example in the re docs
        tokens = [('ADDR', r'/\*[0-9A-Fa-f]{4}\*/'),
                  ('START_VLIW', r'\{'),
                  ('END_VLIW', r'\}'),
                  ('OPCODE', r'/\* 0x[A-Fa-f0-9]+ \*/'),
                  ('SEMICOLON', r';'),
                  ('EOL', r'\n'),
                  ('DISASSEMBLY', r'[^ \t][^;/}]+'),
                  ('WHITESPACE', r'[ \t]+'),
                  ('MISMATCH', r'.')
        ]

        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)

        # for better code
        self._tokens = {}
        for val, (tn, _) in enumerate(tokens, 1):
            self._tokens[val] = tn
            setattr(self, tn, val)

        self._tokens[None] = "End-of-input"

        for lno, l in enumerate(self.data.split('\n')):
            self.line = l

            for m in re.finditer(tok_regex, l + '\n', flags=re.M):
                token = m.lastgroup
                match = m.group()
                self.coord = (lno + 1, m.span())
                self.scoord = f'{self.coord[0]}:{self.coord[1][0]}-{self.coord[1][1]}'

                token_num = getattr(self, token)

                if token_num == self.MISMATCH:
                    self._update_err_pos()
                    self.error(f"Unrecognized token '{match}'")
                elif token_num == self.WHITESPACE:
                    # Sequence?
                    pass
                elif token_num == self.EOL:
                    pass
                else:
                    yield (token_num, match)

            #self._update_err_pos()
            #self.error(f"Encountered end-of-line when scanning {pos}")


    def _update_err_pos(self):
        self.err_coord = self.coord
        self.err_line = self.line
        self.err_scoord = self.scoord

    def lookahead(self):
        return self.token

    def consume(self):
        self._update_err_pos()
        tkn, match = self.token, self.match

        try:
            self.token, self.match = next(self._token_stream)
        except StopIteration:
            self.token, self.match = None, None

        return tkn, match

    def expect(self, token):
        tkn, match = self.consume()
        if tkn == token:
            return match
        else:
            self.error(f"Expecting {self.token_name(token)}, found {self.token_name(tkn)}")

# still line oriented (we don't check that braces for vliw match, for example)
# sched = opcode_binary   # used for scheduling [and for second vliw opcode, but that is matched by disasm]
# disasm = addr vliw_start? opcode_text vliw_end? opcode_binary
# d = (sched | disasm)+

class DisassemblyParser(object):
    def parse(self, disasm, token_stream = None):
        if token_stream is None:
            err = ParseError()
            token_stream = DisassemblyTokenizer(disasm, err)

        out = []
        while True:
            tkn, match = token_stream.consume()

            if tkn == token_stream.ADDR:
                raw = token_stream.err_line
                addr = match[2:-2]

                start_vliw = False
                if token_stream.lookahead() == token_stream.START_VLIW:
                    _, _ = token_stream.consume()
                    start_vliw = True

                disasm, end_vliw, opcode = self.parse_disasm(token_stream)
                opcode = opcode[3:-3]

                # accommodate 10+, but strip linebreak
                if raw != token_stream.err_line:
                    raw = raw + token_stream.err_line

                out.append(SASS_INSN_CUOBJDUMP(loc=addr, opcode=opcode, text=disasm,
                                               raw=raw, vliw_start=start_vliw,
                                               vliw_end = end_vliw))
            elif tkn == token_stream.OPCODE:
                opcode = match[3:-3]
                out.append(SASS_INSN_CUOBJDUMP(loc=None, opcode=opcode, text='',
                                               raw=token_stream.err_line, vliw_start=False,
                                               vliw_end = False))
            elif tkn is None:
                break
            else:
                err.error(token_stream, f"Unexpected token {token_stream.token_name(tkn)}")

        return out

    def parse_disasm(self, token_stream):
        """ disasm ::= disassembly (semicolon | end_vliw) opcode # 10 and beyond
            disasm ::= disassembly semicolon end_vliw? opcode # prior to 10"""

        disasm = token_stream.expect(token_stream.DISASSEMBLY)

        # this tolerates both pre 10 and post 10 representations of VLIW
        lookahead = token_stream.lookahead()
        if lookahead == token_stream.SEMICOLON:
            _, _ = token_stream.consume()
            lookahead = token_stream.lookahead()

        end_vliw = False
        if lookahead == token_stream.END_VLIW:
            end_vliw = True
            _, _ = token_stream.consume()

        opcode = token_stream.expect(token_stream.OPCODE)
        return disasm, end_vliw, opcode


def error_message(tokenizer, message):
    print(f"{tokenizer.scoord}: {message}", file=sys.stderr)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Parse the output of cuobjdump")
    p.add_argument("output", help="Output to parse, must be only part between Function and ...")

    args = p.parse_args()

    with open(args.output, 'r') as f:
        out = []
        for l in f:
            if "Function : " in l:
                continue
            elif ".headerflags" in l:
                continue
            elif "....." in l:
                break
            else:
                out.append(l)

        text = ''.join(out)
        p = DisassemblyParser()
        for l in p.parse(text):
            print(l)
