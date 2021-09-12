opcode = {
    0x00: 'nop',
    0x01: 'move',
    0x02: 'move/from16',
    0x03: 'move/16',
    0x04: 'move-wide',
    0x05: 'move-wide/from16',
    0x06: 'move-wide/16',
    0x07: 'move-object',
    0x08: 'move-object/from16',
    0x09: 'move-object/16',
    0x0A: 'move-result',
    0x0B: 'move-result-wide',
    0x0C: 'move-result-object',
    0x0D: 'move-exception',
    0x0E: 'return-void',
    0x0F: 'return',

    0x10: 'return-wide',
    0x11: 'return-object',
    0x12: 'const/4',
    0x13: 'const/16',
    0x14: 'const',
    0x15: 'const/high16',
    0x16: 'const-wide/16',
    0x17: 'const-wide/32',
    0x18: 'const-wide',
    0x19: 'const-wide/high16',
    0x1A: 'const-string',
    0x1B: 'const-string-jumbo',
    0x1C: 'const-class',
    0x1D: 'monitor-enter',
    0x1E: 'monitor-exit',
    0x1F: 'check-cast',

    0x20: 'instance-of',
    0x21: 'array-length',
    0x22: 'new-instance',
    0x23: 'new-array',
    0x24: 'filled-new-array',
    0x25: 'filled-new-array-range',
    0x26: 'fill-array-data',
    0x27: 'throw',
    0x28: 'goto',
    0x29: 'goto/16',
    0x2A: 'goto/32',
    0x2B: 'packed-switch',
    0x2C: 'sparse-switch',
    0x2D: 'cmpl-float',
    0x2E: 'cmpg-float',
    0x2F: 'cmpl-double',

    0x30: 'cmpg-double',
    0x31: 'cmp-long',
    0x32: 'if-eq',
    0x33: 'if-ne',
    0x34: 'if-lt',
    0x35: 'if-ge',
    0x36: 'if-gt',
    0x37: 'if-le',
    0x38: 'if-eqz',
    0x39: 'if-nez',
    0x3A: 'if-ltz',
    0x3B: 'if-gez',
    0x3C: 'if-gtz',
    0x3D: 'if-lez',
    0x3E: 'unused',
    0x3F: 'unused',

    0x40: 'unused',
    0x41: 'unused',
    0x42: 'unused',
    0x43: 'unused',
    0x44: 'aget',
    0x45: 'aget-wide',
    0x46: 'aget-object',
    0x47: 'aget-boolean',
    0x48: 'aget-byte',
    0x49: 'aget-char',
    0x4A: 'aget-short',
    0x4B: 'aput',
    0x4C: 'aput-wide',
    0x4D: 'aput-object',
    0x4E: 'aput-boolean',
    0x4F: 'aput-byte',

    0x50: 'aput-char',
    0x51: 'aput-short',
    0x52: 'iget',
    0x53: 'iget-wide',
    0x54: 'iget-object',
    0x55: 'iget-boolean',
    0x56: 'iget-byte',
    0x57: 'iget-char',
    0x58: 'iget-short',
    0x59: 'iput',
    0x5A: 'iput-wide',
    0x5B: 'iput-object',
    0x5C: 'iput-boolean',
    0x5D: 'iput-byte',
    0x5E: 'iput-char',
    0x5F: 'iput-short',

    0x60: 'sget',
    0x61: 'sget-wide',
    0x62: 'sget-object',
    0x63: 'sget-boolean',
    0x64: 'sget-byte',
    0x65: 'sget-char',
    0x66: 'sget-short',
    0x67: 'sput',
    0x68: 'sput-wide',
    0x69: 'sput-object',
    0x6A: 'sput-boolean',
    0x6B: 'sput-byte',
    0x6C: 'sput-char',
    0x6D: 'sput-short',
    0x6E: 'invoke-virtual',
    0x6F: 'invoke-super',

    0x70: 'invoke-direct',
    0x71: 'invoke-static',
    0x72: 'invoke-interface',
    0x73: 'unused',
    0x74: 'invoke-virtual/range',
    0x75: 'invoke-super/range',
    0x76: 'invoke-direct/range',
    0x77: 'invoke-static/range',
    0x78: 'invoke-interface-range',
    0x79: 'unused',
    0x7A: 'unused',
    0x7B: 'neg-int',
    0x7C: 'not-long',
    0x7D: 'neg-long',
    0x7E: 'not-long',
    0x7F: 'neg-float',

    0x80: 'neg-double',
    0x81: 'int-to-long',
    0x82: 'int-to-float',
    0x83: 'int-to-double',
    0x84: 'long-to-int',
    0x85: 'long-to-float',
    0x86: 'long-to-double',
    0x87: 'float-to-int',
    0x88: 'float-to-long',
    0x89: 'float-to-double',
    0x8A: 'double-to-int',
    0x8B: 'double-to-long',
    0x8C: 'double-to-float',
    0x8D: 'int-to-byte',
    0x8E: 'int-to-char',
    0x8F: 'int-to-short',

    0x90: 'add-int',
    0x91: 'sub-int',
    0x92: 'mul-int',
    0x93: 'div-int',
    0x94: 'rem-int',
    0x95: 'and-int',
    0x96: 'or-int',
    0x97: 'xor-int',
    0x98: 'shl-int',
    0x99: 'shr-int',
    0x9A: 'ushr-int',
    0x9B: 'add-long',
    0x9C: 'sub-long',
    0x9D: 'mul-long',
    0x9E: 'div-long',
    0x9F: 'rem-long',

    0xA0: 'and-long',
    0xA1: 'or-long',
    0xA2: 'xor-long',
    0xA3: 'shl-long',
    0xA4: 'shr-long',
    0xA5: 'ushr-long',
    0xA6: 'add-float',
    0xA7: 'sub-float',
    0xA8: 'mul-float',
    0xA9: 'div-float',
    0xAA: 'rem-float',
    0xAB: 'add-double',
    0xAC: 'sub-double',
    0xAD: 'mul-double',
    0xAE: 'div-double',
    0xAF: 'rem-double',

    0xB0: 'add-int/2addr',
    0xB1: 'sub-int/2addr',
    0xB2: 'mul-int/2addr',
    0xB3: 'div-int/2addr',
    0xB4: 'rem-int/2addr',
    0xB5: 'and-int/2addr',
    0xB6: 'or-int/2addr',
    0xB7: 'xor-int/2addr',
    0xB8: 'shl-int/2addr',
    0xB9: 'shr-int/2addr',
    0xBA: 'ushr-int/2addr',
    0xBB: 'add-long/2addr',
    0xBC: 'sub-long/2addr',
    0xBD: 'mul-long/2addr',
    0xBE: 'div-long/2addr',
    0xBF: 'rem-long/2addr',

    0xC0: 'and-long/2addr',
    0xC1: 'or-long/2addr',
    0xC2: 'xor-long/2addr',
    0xC3: 'shl-long/2addr',
    0xC4: 'shr-long/2addr',
    0xC5: 'ushr-long/2addr',
    0xC6: 'add-float/2addr',
    0xC7: 'sub-float/2addr',
    0xC8: 'mul-float/2addr',
    0xC9: 'div-float/2addr',
    0xCA: 'rem-float/2addr',
    0xCB: 'add-double/2addr',
    0xCC: 'sub-double/2addr',
    0xCD: 'mul-double/2addr',
    0xCE: 'div-double/2addr',
    0xCF: 'rem-double/2addr',

    0xD0: 'add-int/lit16',
    0xD1: 'sub-int/lit16',
    0xD2: 'mul-int/lit16',
    0xD3: 'div-int/lit16',
    0xD4: 'rem-int/lit16',
    0xD5: 'and-int/lit16',
    0xD6: 'or-int/lit16',
    0xD7: 'xor-int/lit16',
    0xD8: 'add-int/lit8',
    0xD9: 'sub-int/lit8',
    0xDA: 'mul-int/lit8',
    0xDB: 'div-int/lit8',
    0xDC: 'rem-int/lit8',
    0xDD: 'and-int/lit8',
    0xDE: 'or-int/lit8',
    0xDF: 'xor-int/lit8',

    0xE0: 'shl-int/lit8',
    0xE1: 'shr-int/lit8',
    0xE2: 'ushr-int/lit8',
    0xE3: 'unused',
    0xE4: 'unused',
    0xE5: 'unused',
    0xE6: 'unused',
    0xE7: 'unused',
    0xE8: 'unused',
    0xE9: 'unused',
    0xEA: 'unused',
    0xEB: 'unused',
    0xEC: 'unused',
    0xED: 'unused',
    0xEE: 'execute-inline',
    0xEF: 'unused',

    0xF0: 'invoke-direct-empty',
    0xF1: 'unused',
    0xF2: 'iget-quick',
    0xF3: 'iget-wide-quick',
    0xF4: 'iget-object-quick',
    0xF5: 'iput-quick',
    0xF6: 'iput-wide-quick',
    0xF7: 'iput-object-quick',
    0xF8: 'invoke-virtual-quick',
    0xF9: 'invoke-virtual-quick/range',
    0xFA: 'invoke-super-quick',
    0xFB: 'invoke-super-quick/range',
    0xFC: 'unused',
    0xFD: 'unused',
    0xFE: 'unused',
    0xFF: 'unused'
}

# type code list
typecode = {
    0x0000: 'TYPE_HEADER_ITEM',
    0x0001: 'TYPE_STRING_ID_ITEM',
    0x0002: 'TYPE_TYPE_ID_ITEM',
    0x0003: 'TYPE_PROTO_ID_ITEM',
    0x0004: 'TYPE_FIELD_ID_ITEM',
    0x0005: 'TYPE_METHOD_ID_ITEM',
    0x0006: 'TYPE_CLASS_DEF_ITEM',
    0x1000: 'TYPE_MAP_LIST',
    0x1001: 'TYPE_TYPE_LIST',
    0x1002: 'TYPE_ANNOTATION_SET_REF_LIST',
    0x1003: 'TYPE_ANNOTATION_SET_ITEM',
    0x1004: 'TYPE_CLASS_DATA_ITEM',
    0x2001: 'TYPE_CODE_ITEM',
    0x2002: 'TYPE_STRING_DATA_ITEM',
    0x2003: 'TYPE_DEBUG_INFO_ITEM',
    0x2004: 'TYPE_ANNOTATION_ITEM',
    0x2005: 'TYPE_ENCODED_ARRAY_ITEM',
    0x2006: 'TYPE_ANNOTATIONS_DIRECTORY_ITEM'
}

access_flag = {
    0x1: 'public',
    0x2: 'private',
    0x4: 'protected',
    0x8: 'static',
    0x10: 'final',
    0x20: 'synchronized',
    0x40: 'bridge',
    0x80: 'varargs',
    0x100: 'native',
    0x200: 'interface',
    0x400: 'abstract',
    0x800: 'strictfp',
    0x1000: 'synthetic',
    0x2000: 'annotation',
    0x4000: 'enum',
    0x8000: 'unused',
    0x10000: 'constructor',
    0x20000: 'synchronized'
}

access_flag_classes = {
    0x1:    'public',
    0x2:    'private',
    0x4:    'protected',
    0x8:    'static',
    0x10:   'final',
    0x200:  'interface',
    0x400:  'abstract',
    0x1000: 'synthetic',
    0x2000: 'annotation',
    0x4000: 'enum',
}

access_flag_fields = {
    0x1:    'public',
    0x2:    'private',
    0x4:    'protected',
    0x8:    'static',
    0x10:   'final',
    0x40:   'volatile',
    0x80:   'transient',
    0x1000: 'synthetic',
    0x4000: 'enum',
}

access_flag_methods = {
    0x1:     'public',
    0x2:     'private',
    0x4:     'protected',
    0x8:     'static',
    0x10:    'final',
    0x20:    'synchronized',
    0x40:    'bridge',
    0x80:    'varargs',
    0x100:   'native',
    0x400:   'abstract',
    0x800:   'strictfp',
    0x1000:  'synthetic',
    0x10000: 'constructor',
    0x20000: 'declared_synchronized',
}

ACCESS_ORDER = [
    0x1,
    0x4,
    0x2,
    0x400,
    0x8,
    0x10,
    0x80,
    0x40,
    0x20,
    0x100,
    0x800,
    0x200,
    0x1000,
    0x2000,
    0x4000,
    0x10000,
    0x20000
]

field_descriptor = {
    'V': 'void',
    'B': 'byte',
    'C': 'char',
    'D': 'double',
    'F': 'float',
    'I': 'int',
    'J': 'long',
    'S': 'short',
    'Z': 'boolean',
    '[': 'array',
}

type_descriptor = {
    'V': 'void',
    'Z': 'boolean',
    'B': 'byte',
    'S': 'short',
    'C': 'char',
    'I': 'int',
    'J': 'long',
    'F': 'float',
    'D': 'double',
    'L': 'class',
    '[': 'array'
}

visibility_values = {
    0x00: 'VISIBILITY_BUILD',
    0x01: 'VISIBILITY_RUNTIME',
    0x02: 'VISIBILITY_SYSTEM'
}


value_types = {
    0x00: 'VALUE_BYTE',
    0x02: 'VALUE_SHORT',
    0x03: 'VALUE_CHAR',
    0x04: 'VALUE_INT',
    0x06: 'VALUE_LONG',
    0x10: 'VALUE_FLOAT',
    0x11: 'VALUE_DOUBLE',
    0x17: 'VALUE_STRING',
    0x18: 'VALUE_TYPE',
    0x19: 'VALUE_FIELD',
    0x1a: 'VALUE_METHOD',
    0x1b: 'VALUE_ENUM',
    0x1c: 'VALUE_ARRAY',
    0x1d: 'VALUE_ANNOTATION',
    0x1e: 'VALUE_NULL',
    0x1f: 'VALUE_BOOLEAN'
}
