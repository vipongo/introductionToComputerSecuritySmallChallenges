# hex2string

Create a function that converts a text string to a string, containing the hexadecimal representation of the text string.
>>> hex2string('61')
'a'
>>> hex2string('776f726c64')
'world'
>>> hex2string('68656c6c6f')
'hello'

# string2hex

Create a function that converts aa string, containing the hexadecimal representation of a text, to the original text string. Inverse of the hex2string function.
>>> string2hex('a')
'61'
>>> string2hex('hello')
'68656c6c6f'
>>> string2hex('world')
'776f726c64'
>>> string2hex('foo')
'666f6f'

# hex_xor

Create a function that xor bitwise two string that contains a number hexadecimal representations.

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

 
# XOR encryption

https://en.wikipedia.org/wiki/XOR_cipher (Links to an external site.)

https://en.wikipedia.org/wiki/One-time_pad (Links to an external site.)

# encrypt_single_byte_xor

Create a function that encrypts a hexadecimal input with one byte repeating hexadecimal key. 

>>> encrypt_single_byte_xor('aaabbccc','00')
'aaabbccc'
>>> encrypt_single_byte_xor(string2hex('hello'),'aa')
'c2cfc6c6c5'
>>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
'hello'
>>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
'Encrypt and decrypt are the same'

 Remark: Encprytion and decryption are the same algorithm in simple xor encryption case.