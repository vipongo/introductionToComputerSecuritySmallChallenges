from week2 import hex2bin, bin2hex


def hex2string(hex_message):
    '''
    >>> hex2string('61')
    'a'
    >>> hex2string('776f726c64')
    'world'
    >>> hex2string('68656c6c6f')
    'hello'
    '''
    ret = ""
    for i in range(0,len(hex_message),2):
        ret += chr(int(hex_message[i:i+2],16))

    return ret

def string2hex(message):
    '''
    >>> string2hex('a')
    '61'
    >>> string2hex('hello')
    '68656c6c6f'
    >>> string2hex('world')
    '776f726c64'
    >>> string2hex('foo')
    '666f6f'
    '''
    ret = ""

    for c in message:
        ret += hex(ord(c))[2:]

    return ret


def hex_xor(hex1,hex2):
    '''
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
    '''
    #Find the bigger length of the two hex
    target_len = max(len(hex1),len(hex2))

    # Pad both of the input to have the same number of zeroes in binary format
    # rjust because: 123 = 0123, but 123 not equal 1230 in decimal case as well
    bin1 = hex2bin(hex1).rjust(target_len*4,'0')
    bin2 = hex2bin(hex2).rjust(target_len*4,'0')

    bin3 = ""

    for i in range(len(bin1)):
        b1 = bin1[i]
        b2 = bin2[i]

        if b1 == b2:
            bin3 += "0"
        else:
            bin3 += "1"

    return bin2hex(bin3).rjust(target_len,'0')


def create_repeated_key(key,target_len):
    ret = ""

    inner_counter = 0
    for i in range(target_len):
        ret += key[inner_counter]
        inner_counter = (inner_counter + 1) % len(key)

    return ret

def encrypt_single_byte_xor(input_message,key):
    '''
    >>> encrypt_single_byte_xor('aaabbccc','00')
    'aaabbccc'
    >>> encrypt_single_byte_xor(string2hex('hello'),'aa')
    'c2cfc6c6c5'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
    'hello'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
    'Encrypt and decrypt are the same'
    '''
    long_key = create_repeated_key(key,len(input_message))
    return hex_xor(input_message,long_key)


valid_characters = "abcdefghijklmnopqrstuvxyz'- \"ABCDEFGHIJKLMNOPQRSTUVXYZ"
def count_simple_text_chars(string):
    count = 0
    for c in string:
        if c in valid_characters:
            count += 1

    return count

def decrypt_single_byte_xor(cipher):
    '''
    >>> decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480')
    'Hi! You have found me!'
    '''

    # Run a maximum search on the results
    best = None
    best_count = None
    for key in range(256):
        hex_key = hex(key)[2:]
        decrypted_message = hex2string(encrypt_single_byte_xor(cipher,hex_key))

        # We count how many normal characters can be found in a message
        # Results that decrypted message that has the most normal character
        # You can use more sophisticated function to determine is a text normal text or not like character distribution for example.
        actual_count = count_simple_text_chars(decrypted_message)
        if best == None or best_count < actual_count:
            best = decrypted_message
            best_count = actual_count

    return best