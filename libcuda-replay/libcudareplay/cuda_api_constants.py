#!/usr/bin/env python

# Author:       Benjamin Valpey
# Date:         08 Mar 2022
# Filename:     cuda_api_constants.py
# Last Edited:  Tue 08 Mar 2022 04:57:46 PM EST
# Description:  CUDA api constants as defined by the documentation

CUDA_ARRAY_FORMAT_ENUM_MAP = {
    0x01: "CU_AD_FORMAT_UNSIGNED_INT8",
    0x02: "CU_AD_FORMAT_UNSIGNED_INT16",
    0x03: "CU_AD_FORMAT_UNSIGNED_INT32",
    0x08: "CU_AD_FORMAT_SIGNED_INT8",
    0x09: "CU_AD_FORMAT_SIGNED_INT16",
    0x0A: "CU_AD_FORMAT_SIGNED_INT32",
    0x10: "CU_AD_FORMAT_HALF",
    0x20: "CU_AD_FORMAT_FLOAT",
}

CUDA_MEMORYTYPE_ENUM_MAP = {
    0x01: "CU_MEMORYTYPE_HOST",
    0x02: "CU_MEMORYTYPE_DEVICE",
    0x03: "CU_MEMORYTYPE_ARRAY",
    0x04: "CU_MEMORYTYPE_UNIFIED",
}
