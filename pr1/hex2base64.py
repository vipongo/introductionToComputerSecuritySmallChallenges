import codecs
def hex2base64(goodHexString):
    myHexString = goodHexString
    #decode to hexadecimal
    hexadecimal = codecs.decode(myHexString, 'hex')
    #encode to base64
    base64 = codecs.encode(hexadecimal, 'base64').decode()
    print("Here is the result:")
    print(base64)

#Uncomment below for a fast example
#hex2base64('000000010000000001')

#source : https://docs.python.org/3/library/codecs.html