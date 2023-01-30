keynames = {
    29: 'left ctrl',
    42: 'left shift',
    54: 'right shift',
    56: 'left alt',
    97: 'right ctrl',
    99: 'print screen',
    100: 'right alt',
    125: 'left gui',
}

ascii_names = {
    '\u2212': '-',
}

keycodes = {
    'a': 0x04,
    'b': 0x05,
    'c': 0x06,
    'd': 0x07,
    'e': 0x08,
    'f': 0x09,
    'g': 0x0A,
    'h': 0x0B,
    'i': 0x0C,
    'j': 0x0D,
    'k': 0x0E,
    'l': 0x0F,
    'm': 0x10,
    'n': 0x11,
    'o': 0x12,
    'p': 0x13,
    'q': 0x14,
    'r': 0x15,
    's': 0x16,
    't': 0x17,
    'u': 0x18,
    'v': 0x19,
    'w': 0x1A,
    'x': 0x1B,
    'y': 0x1C,
    'z': 0x1D,

    '1': 0x1E,
    '2': 0x1F,
    '3': 0x20,
    '4': 0x21,
    '5': 0x22,
    '6': 0x23,
    '7': 0x24,
    '8': 0x25,
    '9': 0x26,
    '0': 0x27,

    'enter': 0x28,
    'esc': 0x29,
    'backspace': 0x2A,
    'tab': 0x2B,
    'space': 0x2C,
    '-': 0x2D,
    '\U00002212': 0x2D,
    '=': 0x2E,
    '[': 0x2F,
    ']': 0x30,
    '#': 0x31,
    '\\': 0x31,

    ';': 0x33,
    "'": 0x34,
    '`': 0x35,
    ',': 0x36,
    '.': 0x37,
    '/': 0x38,
    'caps lock': 0x39,

    'f1': 0x3A,
    'f2': 0x3B,
    'f3': 0x3C,
    'f4': 0x3D,
    'f5': 0x3E,
    'f6': 0x3F,
    'f7': 0x40,
    'f8': 0x41,
    'f9': 0x42,
    'f10': 0x43,
    'f11': 0x44,
    'f12': 0x45,

    'print screen': 0x46,

    'right': 0x4F,
    'left': 0x50,
    'down': 0x51,
    'up': 0x52,

    'insert': 0x49,
    'home': 0x4A,
    'page up': 0x4B,
    'delete': 0x4C,
    'end': 0x4D,
    'page down': 0x4E,

    'left ctrl': 0xE0,
    'ctrl': 0xE0,
    'left shift': 0xE1,
    'shift': 0xE1,
    'left alt': 0xE2,
    'alt': 0xE2,
    'left gui': 0xE3,
    'gui': 0xE3,
    'right ctrl': 0xE4,
    'right shift': 0xE5,
    'right alt': 0xE6,
    'right gui': 0xE7,
}


def get_key_name(event):
    name = keynames.get(event.scan_code, event.name)
    return ascii_names.get(name, name)
