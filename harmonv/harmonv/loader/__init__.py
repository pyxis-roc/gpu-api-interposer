# SPDX-FileCopyrightText: 2019 University of Rochester
#
# SPDX-License-Identifier: MIT

from harmonv import nvfatbin
import logging
_logger = logging.getLogger(__name__)

def extract_elf(module, compute_capability):
    """Extract ELF that are relevant to compute capability"""
    arch = compute_capability[0] * 10 + compute_capability[1]

    elf = []
    for c in module.cubins:
        for cc in c.parts:
            if cc.type == nvfatbin.CUBIN_ELF:
                if cc.arch != arch:
                    #TODO: possibly define a binary_compatible relation
                    _logger.debug(f'Skipping over ELF for arch {cc.arch} (need {arch})')
                else:
                    _logger.info(f'Found exact match for arch {arch} (type {cc.type})')
                    elf.append(cc)

    # TODO: extract symbols
    # TODO: remove empty elf sections
    return elf

def extract_ptx(module, compute_capability):
    """Extract PTX that are relevant to compute capability"""
    arch = compute_capability[0] * 10 + compute_capability[1]

    exact = []
    ptx = []
    for c in module.cubins:
        for cc in c.parts:
            if cc.type == nvfatbin.CUBIN_PTX:
                if cc.arch == arch:
                    _logger.info(f'Found exact PTX match for arch {arch} (type {cc.type})')
                    exact.append(cc)
                else:
                    #TODO: define a ptx_compatible relation for arch != arch
                    #TODO: ptx support by hardware/compiler/runtime?
                    # if by hardware, can we throw out unsupported ptx?
                    ptx.append(cc)

    # TODO: extract symbols
    # TODO: remove empty elf sections
    # TODO: sort ptx
    return (exact, ptx)
