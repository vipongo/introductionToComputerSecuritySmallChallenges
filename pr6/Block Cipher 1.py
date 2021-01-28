from Crypto.Cipher import AES


def decrypt_aes(enc, key, iv):
    """>>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
    >>> iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
    >>> decrypt_aes(bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171]),key,iv)
    b'hello world 1234'
    >>> decrypt_aes(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64]),key,iv)
    b'lovecryptography'"""


    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(enc)


def bit_permutation(bitString, permutation):
    """
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
    """
    current_bit = ""
    for element in permutation:
        current_bit = current_bit + bitString[element - 1]
    return current_bit


def left_shift_rot(bitString, pad=1):
    """
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
    """
    current_bit = ""
    current = 0
    for element in range(len(bitString)):
        if element + pad != len(bitString):
            current_bit = current_bit + bitString[element + pad]
        else:
            while current != pad:
                current_bit = current_bit + bitString[current]
                current = current + 1
            break
    return current_bit


def PKCS7_pad(message, number):
    """
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
    """

    padValue = int(number - len(message)) % number

    if padValue == 0:
        return message + chr(number) * number
    else:
        return message + chr(padValue) * padValue


if __name__ == "__main__":
    import doctest

    doctest.testmod()
