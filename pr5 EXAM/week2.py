def hex2bin(hex_value):
    '''
    >>> hex2bin('f')
    '1111'
    >>> hex2bin('1')
    '1'
    '''
    return bin(int(hex_value, 16))[2:]

def bin2hex(binary):
    '''
    >>> bin2hex('1111')
    'f'
    >>> bin2hex('1')
    '1'
    '''
    return hex(int(binary,2))[2:]

def fillupbyte(binary):
    '''
    >>> fillupbyte('011')
    '00000011'
    >>> fillupbyte('1')
    '00000001'
    >>> fillupbyte('10111')
    '00010111'
    >>> fillupbyte('11100111')
    '11100111'
    '''
    target_length = len(binary) + (8 - len(binary) % 8) % 8
    return binary.zfill(target_length)


def binary2base64(binary):
    padded_binary = binary.ljust(len(binary) + (6 - len(binary) % 6) % 6, '0')
    ret = ""
    while len(padded_binary) > 0:
        actual_bit_sequence = padded_binary[:6]
        padded_binary = padded_binary[6:]
        v = int(actual_bit_sequence, 2)
        ret += base64_table[v]

    while len(ret) % 4 != 0:
        ret += "="

    return ret

base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def int2base64(value):
    '''
    >>> int2base64(0x61)
    'YQ=='
    >>> int2base64(0x78)
    'eA=='
    '''
    binary = fillupbyte(bin(value)[2:])
    return binary2base64(binary)



def hex2base64(hex_value):
    '''
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    >>> hex2base64('7368726f6f6d')
    'c2hyb29t'
    '''
    binary = fillupbyte(hex2bin(hex_value))
    return binary2base64(binary)
