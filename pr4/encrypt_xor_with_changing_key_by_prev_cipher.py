def encrypt_by_add_mod(message ,key):
    """
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    """
    res = ""
    for element in message:
        charBin = ord(element)
        result = (charBin + key)%256
        result = chr(result)
        res = res + result
    return res

def encrypt_xor_with_changing_key_by_prev_cipher(value, key, encryOrDecrypt):
    """
    >>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
    '3V:V9'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    """
    res = ""
    if(encryOrDecrypt == "encrypt"):
        result = key
        for element in value:
            charBin = ord(element)
            result = (charBin ^ result)
            result1 = chr(result)
            res = res + result1
        return res
    else:
        inverse = ""
        for element in value:
            inverse = element + inverse 
        result = ord(inverse[len(inverse)-1])
        for element in inverse:
            charBin = ord(element)
            result = (charBin ^ result)
            result1 = chr(result)
            res = result1 + res
            result = ord(element)
        result = key
        charBin = ord(element)
        result = (charBin ^ result)
        result1 = chr(result)
        res = result1 + res
        return res[:len(res)-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()