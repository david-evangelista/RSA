# INSE 6110, F-2021
# Programming Project 
# David Evangelista
#   RSA: p, q, n, e generation
import binascii

#----- Text Conversion -----
def hex_to_str(array):
    s = ""
    for i in array:  
        s += binascii.unhexlify(i)
    return s

#----- Convert to Binary -----
# converts a given string to chunks of 3 letters in binary
def str_to_nbr(message):
    print("converting string \""+message+"\" to numbers...")
    #pad message with spaces so that length is multiple of 3
    if (len(message) % 3) == 1:
        message = message+"  "
    #how many 3-letter chunks
    if (len(message) % 3) == 2:
        message = message+" "
    a_byte_array = bytearray(message, "utf8")
    converted = []

    for byte in a_byte_array:
        converted.append(hex(byte)[2:])
    #Add to list
    converted = ''.join(converted)
    converted = [converted[i:i+6] for i in range(0, len(converted), 6)]
    decimal = []
    for i in converted:
        decimal.append(int(i, 16))
    print(decimal)    
    return decimal




