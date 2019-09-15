all: PtxParser.py ptx_ast.py

ptx_ast.py: _ptx_ast.cfg _build_ast.py _ast_gen.py
	python3 _build_ast.py

PtxParser.py: Ptx.g4
	antlr4 -Dlanguage=Python3 -visitor Ptx.g4

.phony: clean

clean:
	rm -f Ptx.interp Ptx.tokens PtxLexer.interp PtxLexer.py PtxLexer.tokens PtxListener.py PtxParser.py
