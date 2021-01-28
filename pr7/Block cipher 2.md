# decrypt_aes_ecb

Last week we used the AES library in CBC mode. Now create a function that uses the same library and decrypt a message that is coded in ECB mode.

https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_(ECB) (Links to an external site.)

>>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
>>> decrypt_aes_ecb(bytes([215, 221, 59, 138, 96, 94, 155, 69, 52, 90, 212, 108, 49, 65, 138, 179]),key)
b'lovecryptography'
>>> decrypt_aes_ecb(bytes([147, 140, 44, 177, 97, 209, 42, 239, 152, 124, 241, 175, 202, 164, 183, 18]),key)
b'!!really  love!!'

# xor_byte_arrays

Create a function that xors two byte array.  Not that you can use rjust on byte strings arrays as well, like input1_padded = input1.rjust(max_len,bytes([0]))

>>> xor_byte_arrays(bytes([1,2,3,4]),bytes([2,3,4,5]))
b'\\x03\\x01\\x07\\x01'
>>> xor_byte_arrays(bytes([1,2,3,4]),bytes([]))
b'\\x01\\x02\\x03\\x04'
>>> xor_byte_arrays(bytes([1,2,3,4]),bytes([1,2]))
b'\\x01\\x02\\x02\\x06'
>>> xor_byte_arrays(bytes([1,2,4,8,16,32,64,128]),bytes([1,1,1,1,1,1,1,1]))
b'\\x00\\x03\\x05\\t\\x11!A\\x81'

Remarks

    Understand the examples before start. e.g.: 0x81=129
    b'\x00\x03\x05\t\x11!A\x81' = bytes([0,3,5,9,17,33,65,129]) You can test it in python with:

print(b'\x00\x03\x05\t\x11!A\x81' == bytes([0,3,5,9,17,33,65,129]))

    In test docs you have to escape the \ characters with a \, that is why every \ is doubled.

# decrypt_aes_cbc_with_ecb

Implement AES in CBC mode with the previous function. This function must produce the same result as the last week function (so the test cases are same). ECB mode is the core of the encryption without any chaining. In CBC mode you have some extra xoring: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_(CBC) (Links to an external site.)

Every encryption CBC encryption method can be built from the implementation of the ECB mode.

>>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
>>> iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
>>> decrypt_aes_cbc_with_ecb(bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171]),key,iv)
b'hello world 1234'
>>> decrypt_aes_cbc_with_ecb(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64]),key,iv)
b'lovecryptography'

# encrypt_aes_cbc_with_ecb

Create a function that implements the AES encryption in CBC mode, using only AES in ECB mode.

>>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
>>> iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
>>> encrypt_aes_cbc_with_ecb(b'hello world 1234',key,iv)
b'\\xff\\x12Cs\\xacu\\xf2\\xe9\\xf6EQ\\x9c4\\x9a{\\xab'
>>> encrypt_aes_cbc_with_ecb(bytes(b'lovecryptography'),key,iv)
b'\\xab\\xda\\xa0`\\xc1\\x86IQ\\xdd\\x95\\x13\\xb4\\x1f\\xf7j@'

Do not forget:

b'\\xff\\x12Cs\\xacu\\xf2\\xe9\\xf6EQ\\x9c4\\x9a{\\xab' 

equals to

bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171])