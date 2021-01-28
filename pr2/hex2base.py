
#convert hexadecimal to binary 
def hex2bin(value):
    ''''
    >>> hex2bin('f')
    '1111'
    >>> hex2bin('5')
    '101'
    >>> hex2bin('1')
    '1'
    '''
    return bin(int(value, 16))[2:]

#convert binary to hexadecimal 
def bin2hex(value):
    '''
    >>> bin2hex('1111')
    'f'
    >>> bin2hex('100001')
    '21'
    >>> bin2hex('1')
    '1'
    '''
    return hex(int(value, 2))[2:]

#fill uncompleted byte (ex: "001" => "00000001")
def fillupbyte(value):
    '''
    >>> fillupbyte('011')
    '00000011'
    >>> fillupbyte('1')
    '00000001'
    >>> fillupbyte('10111')
    '00010111'
    >>> fillupbyte('11100111')
    '11100111'
    >>> fillupbyte('111001111')
    '0000000111001111'
    '''
    fillupbyte = value
    length = len(value)
    if (length%8 != 0):
        toAdd = 8 - (length%8)
        for _ in range(toAdd):
            fillupbyte = "0" + fillupbyte
    return fillupbyte

#convert integer to base64
def int2base64(value):
    '''
    >>> int2base64(0x61)
    'YQ=='
    >>> int2base64(0x78)
    'eA=='
    '''
    base64List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    binaryValue= fillupbyte(bin(value)[2:])
    length = len(binaryValue)
    res = ""
    for _ in range (int(length/6)+1):
        if(length <= 6):
            for _ in range (6 - length):
                binaryValue = binaryValue + "0"
            index = int(binaryValue[0:6], 2)
            res = res + base64List[index]
            break

        index = int(binaryValue[0:6], 2)
        res = res + base64List[index]
        binaryValue = binaryValue[6:]
        length = length-6


    res = res + "=="
    return res

# converts a string, containing the hex representaion of a number, to base64.
def hex2base64(value):
    '''
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    '''
    base64List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    binaryValue = fillupbyte(hex2bin(value))
    length = len(binaryValue)
    res = ""
    for _ in range (int(length/6)+1):
        if(length <= 6):
            for _ in range (6 - length):
                binaryValue = binaryValue + "0"
            index = int(binaryValue[0:6], 2)
            res = res + base64List[index]
            break

        index = int(binaryValue[0:6], 2)
        res = res + base64List[index]
        binaryValue = binaryValue[6:]
        length = length-6


    res = res + "=="
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()



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
    intIntputbyte = int(inputbyte)
    return bytes([b ^ intIntputbyte for b in bytes(value)])