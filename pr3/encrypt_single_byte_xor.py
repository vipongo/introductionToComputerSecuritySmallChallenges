def hex2string(value):
    """
    >>> hex2string('61')
    'a'
    >>> hex2string('776f726c64')
    'world'
    >>> hex2string('68656c6c6f')
    'hello'
    """
    res = ""
    while(value !=""):
        res = res + chr(int(value[:2], base=16))
        value = value[2:]
    return res

def string2hex(value):
    """
    >>> string2hex('a')
    '61'
    >>> string2hex('hello')
    '68656c6c6f'
    >>> string2hex('world')
    '776f726c64'
    >>> string2hex('foo')
    '666f6f'
    """
    
    return "".join("{:02x}".format(ord(chara)) for chara in value)



def hex_xor(value1, value2):
    """
    >>> hex_xor('aabbf11','12345678')
    '189fe969'
    >>> hex_xor('12cc','12cc')
    '0000'
    >>> hex_xor('1234','2345')
    '3171'
    >>> hex_xor('111','248')
    '359'
    >>> hex_xor('8888888','1234567')
    '9abcdef'
    """
    result = hex(int(value1, 16) ^ int(value2, 16))[2:]
    while len(result) < len(value1):
        result = "0" + result
    return result

def encrypt_single_byte_xor(value, inputbyte):
    """
    >>> encrypt_single_byte_xor('aaabbccc','00')
    'aaabbccc'
    >>> encrypt_single_byte_xor(string2hex('hello'),'aa')
    'c2cfc6c6c5'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
    'hello'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
    'Encrypt and decrypt are the same'
    """
    multipliedInputByte = inputbyte * int(len(value)/2)
    return hex_xor(value, multipliedInputByte)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


#loop to find the key
#for key in range(0xff):

key = 0xa1
print(hex2string(encrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480', hex(key)[2:])) + ' : The key is: ' +  hex(key)[2:])

#a1: Hi! You have found me!
