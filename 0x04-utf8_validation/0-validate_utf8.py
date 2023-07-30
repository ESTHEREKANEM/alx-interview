#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    def get_byte_count(byte):
        if byte & 0x80 == 0:
            return 1
        elif byte & 0xE0 == 0xC0:
            return 2
        elif byte & 0xF0 == 0xE0:
            return 3
        elif byte & 0xF8 == 0xF0:
            return 4
        else:
            return -1

    i = 0
    while i < len(data):
        byte_count = get_byte_count(data[i])
        if byte_count == -1:
            return False

        if i + byte_count > len(data):
            return False

        for j in range(1, byte_count):
            if (data[i + j] & 0xC0) != 0x80:
                return False

        i += byte_count

    return True

