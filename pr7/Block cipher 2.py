from Crypto.Cipher import AES

decrypted += decrypt_aes_ecb(xor_byte_arrays(piece, prev_piece), key)

def decrypt_aes_ecb(enc, key):
    """
    >>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
    >>> decrypt_aes_ecb(bytes([215, 221, 59, 138, 96, 94, 155, 69, 52, 90, 212, 108, 49, 65, 138, 179]),key)
    b'lovecryptography'
    >>> decrypt_aes_ecb(bytes([147, 140, 44, 177, 97, 209, 42, 239, 152, 124, 241, 175, 202, 164, 183, 18]),key)
    b'!!really  love!!'
"""
    decipher = AES.new(key, AES.MODE_ECB)
    return decipher.decrypt(enc)

def xor_byte_arrays(array1, array2):
    """
    >>> xor_byte_arrays(bytes([1,2,3,4]),bytes([2,3,4,5]))
    b'\\x03\\x01\\x07\\x01'
    >>> xor_byte_arrays(bytes([1,2,3,4]),bytes([]))
    b'\\x01\\x02\\x03\\x04'
    >>> xor_byte_arrays(bytes([1,2,3,4]),bytes([1,2]))
    b'\\x01\\x02\\x02\\x06'
    >>> xor_byte_arrays(bytes([1,2,4,8,16,32,64,128]),bytes([1,1,1,1,1,1,1,1]))
    b'\\x00\\x03\\x05\\t\\x11!A\\x81'
    """
    if (len(array2) < len(array1)):
        array2 = array2.rjust(len(array1),bytes([0]))

    result = bytearray(len(array1))

    for i in range(len(array1)):
        result[i] = (array1[i] ^ array2[i])

    return bytes(result)

def decrypt_aes_cbc_with_ecb(enc, key, iv):
    """
    >>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
    >>> iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
    >>> decrypt_aes_cbc_with_ecb(bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171]),key,iv)
    b'hello world 1234'
    >>> decrypt_aes_cbc_with_ecb(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64]),key,iv)
    b'lovecryptography'
    """
    prev_piece = iv
    decrypted = []
    for i in range(0, len(enc), 16):
        piece = enc[i : i + 16]
        decrypted += xor_byte_arrays(decrypt_aes_ecb(piece, key), prev_piece)
        prev_piece = piece
        result = decrypt_aes_ecb(input_bytes, key)
        xor = xor_byte_arrays(iv, result)
        return xor
    return bytes(decrypted)


def encrypt_aes_cbc_with_ecb(enc, key, iv):
    """
    >>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
    >>> iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
    >>> encrypt_aes_cbc_with_ecb(b'hello world 1234',key,iv)
    b'\\xff\\x12Cs\\xacu\\xf2\\xe9\\xf6EQ\\x9c4\\x9a{\\xab'
    >>> encrypt_aes_cbc_with_ecb(bytes(b'lovecryptography'),key,iv)
    b'\\xab\\xda\\xa0`\\xc1\\x86IQ\\xdd\\x95\\x13\\xb4\\x1f\\xf7j@'
    >>> encrypt_aes_cbc_with_ecb(b'hello world 1234hello world 1234hello world 1234',key,iv)
    b'\\xff\\x12Cs\\xacu\\xf2\\xe9\\xf6EQ\\x9c4\\x9a{\\xab>\\xe3\\xc3\\xf5g\\xc7kYZpk>\\x88\\xf3\\x0f\\x16\\x13\\x85\\xb5\\x1d\\r+\\xdc\\xae\\xa1\\x1d\\x80\\xfa_F\\xb1\\xc0'
    >>> encrypt_aes_cbc_with_ecb(bytes(b'lovecryptography123456789abcdefhellooooooooooooo'),key,iv)
    b'\\xab\\xda\\xa0`\\xc1\\x86IQ\\xdd\\x95\\x13\\xb4\\x1f\\xf7j@\\xd7\\xf2\\xd1T\\xfe[\\xd1\\xb4d5\\x90\\xdc\\x1fj?\\x12\\xfd\\x15\\xcb\\x8b\\xa3\\x1c*\\xd4B\\x8fJs\\x03\\xf9\\x7f3'
    """

    prev_piece = iv
    encrypted = []

    for i in range(0, len(enc), 16):
        piece = enc[i : i + 16]
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted_block = cipher.encrypt(xor_byte_arrays(piece, prev_piece))
        encrypted += encrypted_block
        prev_piece = encrypted_block
    return bytes(encrypted)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
