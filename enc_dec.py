# INSE 6110, F-2021
# Programming Project 
# David Evangelista
#   RSA: encryption/decryption

from text_conv import str_to_nbr, hex_to_str

def rsa_array_nbrs(n, exp, array_nbrs):
    new_arr = []
    print("... decrypting (note this is in hex)...")
    for i in array_nbrs:
        nbr = int(i, 10)
        #perform rsa operation, convert to hex, append to array
        s = (hex(int(rsa(n, exp, nbr)))[2:])
        # pad with 0's
        while len(s) < 8:
           s = "0"+s
        new_arr.append(s)   
    #convert to hex    
    print(new_arr)
    print("... converting hex values to string...")
    print (hex_to_str(new_arr))


def rsa_str(n, exp, str):
    #convert the string to numbers and prints
    array = str_to_nbr(str)
    new_arr = []
    print("... encrypting...")   
    for i in array:
        #perform rsa operation, append to new array
        new_arr.append(int(rsa(n, exp, i)))
    print(new_arr) 
    return new_arr


#----- RSA Encryption / Decryption function -----
# encrypts a message m / decrypts a cipher c
def rsa(n, exp, val):
    result = 1  
    # create a list of binary representing exponent
    exp_bin = [int(d) for d in str(bin(exp)[2:])]
    # place msg/cipher at end of list
    val_bin = [val]
    # create list of squared values
    for i in range(1, len(exp_bin)):
        val = val*val % n
        val_bin.insert(0, val)
    # iterate and when exponent != 0, multiply, else pass
    for i in range(0, len(exp_bin)):
        if exp_bin[i] == 0:
            pass
        else:
            result *= exp_bin[i] * val_bin[i] % n
    return result % n

