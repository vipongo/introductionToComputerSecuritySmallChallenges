
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from week6 import bit_permutation, left_shift_rot

#This assignment has been realised also following these tutorials and ideas
#https://medium.com/@urwithajit9/how-to-teach-des-using-python-the-easy-way-part-1-des-subkey-generation-bb5a853ef9b0
#https://gist.github.com/BlackRabbit-github/2924939




# tables for key generation
key_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63,
       55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# tables for encryption

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
IP_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]


# Tables for function f

E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

S = \
[
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25]

def bytes2binary(inputBytes):
    """
    >>> bytes2binary(b'\\x01')
    '00000001'
    >>> bytes2binary(b'\\x03')
    '00000011'
    >>> bytes2binary(b'\\xf0')
    '11110000'
    >>> bytes2binary(b'\\xf0\\x80')
    '1111000010000000'
    """
    result = 0
    for i in inputBytes:
        result = result * 256 + int(i)
    return bin(result)[2:].rjust(len(inputBytes*8), "0")


def binary2bytes(inputBin):
    """
    >>> binary2bytes('00000001')
    b'\\x01'
    >>> binary2bytes('00000011')
    b'\\x03'
    >>> binary2bytes('11110000')
    b'\\xf0'
    >>> binary2bytes('1111000010000000')
    b'\\xf0\\x80'
    """
    #check if length is divisible by 8
    if len(inputBin) % 8 == 0:
        byteList = []
        for i in range(0, len(inputBin), 8):
            #convert each 8 bits in int
            byteList += [int(inputBin[i:i+8], 2)]

        #convert the list to bytes
        return bytes(byteList)

    #recursive to send back with a length divisable by 8
    else:
        return binary2bytes(inputBin.rjust(len(inputBin) + 8-len(inputBin) % 8, "0"))

def bin_xor(inputBin1, inputBin2):
    """
    >>> bin_xor('1011','0000')
    '1011'
    >>> bin_xor('1','0000')
    '0001'
    >>> bin_xor('1101','1011')
    '0110'
    >>> bin_xor('10101010','01010101')
    '11111111'
    """
    result = ""

    #We set each binary input to the same length by adding zeroes on the left to the smaller one
    if len(inputBin1) > len(inputBin2):
        inputBin2 = inputBin2.rjust(len(inputBin1), "0")
    else:
        inputBin1 = inputBin1.rjust(len(inputBin2), "0")

    #we check if each bit is equal
    for id in range(len(inputBin1)):
        if inputBin1[id] == inputBin2[id]:
            result += "0"
        else : 
            result += "1"
    return result

def create_DES_subkeys(key):
    """
    >>> create_DES_subkeys('0001001100110100010101110111100110011011101111001101111111110001')
    ['000110110000001011101111111111000111000001110010', '011110011010111011011001110110111100100111100101', '010101011111110010001010010000101100111110011001', '011100101010110111010110110110110011010100011101', '011111001110110000000111111010110101001110101000', '011000111010010100111110010100000111101100101111', '111011001000010010110111111101100001100010111100', '111101111000101000111010110000010011101111111011', '111000001101101111101011111011011110011110000001', '101100011111001101000111101110100100011001001111', '001000010101111111010011110111101101001110000110', '011101010111000111110101100101000110011111101001', '100101111100010111010001111110101011101001000001', '010111110100001110110111111100101110011100111010', '101111111001000110001101001111010011111100001010', '110010110011110110001011000011100001011111110101']
    """
    # permutation with the original key
    fullKey = bit_permutation(key, PC1)

    #we split the key into right and left part
    lprev, rprev = fullKey[:28], fullKey[28:]

    nFinalBlock = []
    #We now proceed through 16 iterations, for 1<=n<=16
    for n in range (16):
        lPart, rPart = left_shift_rot(lprev, key_shifts[n]), left_shift_rot(rprev, key_shifts[n])
        lprev, rprev = lPart, rPart
        nFinalBlock += ["".join([lPart, rPart])]

    #We now form the keys Kn, for 1<=n<=16, by applying the following permutation table to each of the concatenated pairs rPart, lPart
    nPrimeFinalBlock = []
    for n in range(16):
        nPrimeFinalBlock += [bit_permutation(nFinalBlock[n], PC2)]

    return nPrimeFinalBlock
def f(rn ,finalBlock):
    """
    >>> f('11110000101010101111000010101010','000110110000001011101111111111000111000001110010')
    '00100011010010101010100110111011'
    """
    expPerm = bit_permutation(rn, E)

    # XOR with the key
    xored = bin_xor(finalBlock, expPerm)

    #split up into 6-bit long blocks
    bList = []
    for i in range(0, len(xored), 6):
        bList.append(xored[i:i+6])


    sList = []
    for n in range(8):
        row = int("".join([bList[n][0], bList[n][5]]), 2)
        column = int("".join([bList[n][i]for i in range(1,5)]), 2)
        sList.append(bin(S[n][row][column])[2:].rjust(4, '0'))
    SList = "".join(sList)

    # Straight Permutation
    return bit_permutation(SList, P)


def encrypt_DES(key, plainText):
    """
    >>> encrypt_DES(b'\\x13\\x34\\x57\\x79\\x9b\\xbc\\xdf\\xf1',b'\\x01\\x23\\x45\\x67\\x89\\xab\\xcd\\xef')
    b'\\x85\\xe8\\x13T\\x0f\\n\\xb4\\x05'
    """
    #create subKeys:
    subKeyList = create_DES_subkeys(bytes2binary(key))
    #we do the initial permutation of the plainText
    initPerm = bit_permutation(bytes2binary(plainText),IP)

    final = ''
    lPrev, rPrev = initPerm[:32], initPerm[32:]
    for n in range(16):
        lPart, rPart = rPrev, bin_xor(lPrev, f(rPrev, subKeyList[n]))
        lPrev, rPrev = lPart, rPart
        final = "".join([rPart, lPart])

    # Final Permutation:

    return binary2bytes(bit_permutation(final, IP_inverse))


def are_random_tests_all_passes(numberOfTests):
    """
    >>> are_random_tests_all_passes(100)
    True
    """
    for _ in range(numberOfTests):
        # Generate two randome 8 bytes long and set them to the plain text and the key
        plainText = get_random_bytes(8)
        key = get_random_bytes(8)

        # We use our own encryption function with the plain text and the key
        createdDES = encrypt_DES(key, plainText)

        # We use the build in encryption function from Cipher with the plain text and the key
        cipher = DES.new(key, DES.MODE_ECB)
        builtInDES = cipher.encrypt(plainText)

        # compare both runs, if the same: output = 'False'
        if (builtInDES != createdDES):
            return False
        
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()