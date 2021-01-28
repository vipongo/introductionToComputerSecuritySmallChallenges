Every tasks builds on the previous tasks, keep it in mind and solve the tasks in order. The main goal now to implement the simple DES algorithm and understand how it works.

You can find a detailed document of simple DES on TU Berlin: http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm (Links to an external site.)

The TU Berlin document is a well-detailed document, my advise to use that, but you can use any source if you think, but be careful.:)

You can find a video that explains the TU Berlin document: https://www.youtube.com/watch?v=GOLN3h-M9GA

This video contains error in the number example, so be careful: https://www.youtube.com/watch?v=Sy0sXa73PZA

On this link you can find the matrices in python, you can copy paste it into your code:

Week 8. - DES matrices
# bytes2binary

Implement a function that converts array of bytes to a string containing the binary representation of the input.

>>> bytes2binary(b'\\x01')
'00000001'
>>> bytes2binary(b'\\x03')
'00000011'
>>> bytes2binary(b'\\xf0')
'11110000'
>>> bytes2binary(b'\\xf0\\x80')
'1111000010000000'

# binary2bytes

Implement a function that converts a string containing the binary representation to array of bytes.

>>> binary2bytes('00000001')
b'\\x01'
>>> binary2bytes('00000011')
b'\\x03'
>>> binary2bytes('11110000')
b'\\xf0'
>>> binary2bytes('1111000010000000')
b'\\xf0\\x80'

# bin_xor

Implement a binary xor function.

>>> bin_xor('1011','0000')
'1011'
>>> bin_xor('1','0000')
'0001'
>>> bin_xor('1101','1011')
'0110'
>>> bin_xor('10101010','01010101')
'11111111'

# create_DES_subkeys

Implement the key generation function of simple DES encryption scheme.

>>> create_DES_subkeys('0001001100110100010101110111100110011011101111001101111111110001')
['000110110000001011101111111111000111000001110010', '011110011010111011011001110110111100100111100101', '010101011111110010001010010000101100111110011001', '011100101010110111010110110110110011010100011101', '011111001110110000000111111010110101001110101000', '011000111010010100111110010100000111101100101111', '111011001000010010110111111101100001100010111100', '111101111000101000111010110000010011101111111011', '111000001101101111101011111011011110011110000001', '101100011111001101000111101110100100011001001111', '001000010101111111010011110111101101001110000110', '011101010111000111110101100101000110011111101001', '100101111100010111010001111110101011101001000001', '010111110100001110110111111100101110011100111010', '101111111001000110001101001111010011111100001010', '110010110011110110001011000011100001011111110101']

f

Implement the core f function of the simple DES encryption scheme.

>>> f('11110000101010101111000010101010','000110110000001011101111111111000111000001110010')
'00100011010010101010100110111011'

# encrypt_DES

Implement the simple DES encryption scheme.

>>> encrypt_DES(b'\\x13\\x34\\x57\\x79\\x9b\\xbc\\xdf\\xf1',b'\\x01\\x23\\x45\\x67\\x89\\xab\\xcd\\xef')
b'\\x85\\xe8\\x13T\\x0f\\n\\xb4\\x05'

# are_random_tests_all_passes

Create a function that run random tests and compare your solution results to an existing one.

In one step the function generates a random key and a message (8-8bytes) and run the DES algorithm in ECB mode, from the Crypto.cipher library. After that run your encryption algorithm with the same key and message and compare the two result multiple times (the argument determines how many run you have to do). If all test was successful, return True. The only parameter of the function is the number of tests.

>>> are_random_tests_all_passes(100)
True