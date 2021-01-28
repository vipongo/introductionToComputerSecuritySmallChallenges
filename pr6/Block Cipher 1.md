Theoretically you should know what block cipher and padding is, but you can refresh your overview knowledge about the topic on the following links:

https://www.youtube.com/watch?v=RiCaySI-H8A&list=PLNQ0TotYXRCVyjoO-XcLT9n_H0oeNdNBD (Links to an external site.)

        
      

https://en.wikipedia.org/wiki/Padding_(cryptography) (Links to an external site.)

You will need in the following to know what the difference between string and bytes in python3, read this:
https://www.geeksforgeeks.org/byte-objects-vs-string-python/ (Links to an external site.)

# AES

Create a function that decrypts a message with AES CBC mode with the given IV and key. Here you must use an external AES library that implements the encprytion scheme.

https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html (Links to an external site.)

>>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
>>> iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
>>> decrypt_aes(bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171]),key,iv)
b'hello world 1234'
>>> decrypt_aes(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64]),key,iv)
b'lovecryptography'

# bit_permutation

Create a function that permutate a binary string. The first parameter will be permutated. The second parameter determines that which bits of the original string will comes next. In the second test case the outputs first bit will be third bit of the source, the output second bit will be the second bit of the source, and the third bit of the output will be the first bit of the source. 

>>> bit_permutation("101",[1,2,3])
'101'
>>> bit_permutation("101",[3,2,1])
'101'
>>> bit_permutation("101",[1,3,2])
'110'
>>> bit_permutation("101",[3,2,1])
'101'
>>> bit_permutation("1010",[3,4,1,2])
'1010'
>>> bit_permutation("1010",[1,3,2,4])
'1100'
>>> bit_permutation("11110000",[5,6,7,8,1,2,3,4])
'00001111'
>>> bit_permutation("0001001100110100010101110111100110011011101111001101111111110001",[57,49, 41,33, 25, 17, 9,1,58, 50,42, 34, 26,18,10, 2, 59,51, 43, 35,27,19,11,  3,60, 52, 44,36,63,55, 47,39, 31, 23,15,7,62, 54,46, 38, 30,22,14, 6, 61,53, 45, 37,29,21,13,  5,28, 20, 12, 4])
'11110000110011001010101011110101010101100110011110001111'

# bit_rotation

Create a function that rotates a string, containing a binary represented number, to the left with the given step.

>>> left_shift_rot('010')
'100'
>>> left_shift_rot('111')
'111'
>>> left_shift_rot('1010111001')
'0101110011'
>>> left_shift_rot('0101110011')
'1011100110'
>>> left_shift_rot('1010111001',2)
'1011100110'
>>> left_shift_rot('0001',3)
'1000'

# PKCS#7 padding

Create a function that pads a given text string with PKCS#7 padding.

https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS#5_and_PKCS#7 (Links to an external site.)

>>> PKCS7_pad('hello',6)
'hello\\x01'
>>> PKCS7_pad('hello',7)
'hello\\x02\\x02'
>>> PKCS7_pad('hello, how are you?',26)
'hello, how are you?\\x07\\x07\\x07\\x07\\x07\\x07\\x07'
>>> PKCS7_pad('hello, how are you?',55)
'hello, how are you?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
>>> PKCS7_pad('hello, how are you?',67)
'hello, how are you?000000000000000000000000000000000000000000000000'