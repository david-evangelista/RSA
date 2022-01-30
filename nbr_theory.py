# INSE 6110, F-2021
# Programming Project 
# David Evangelista
#   RSA: number theory

import math

#----- Number Theory -----

#----- Is Prime -----
# determines whether a given number is prime
def is_prime(nbr):
    #iterates from 2 until the square root of the given number
    for i in range(2, int (math.ceil(math.sqrt(nbr)))):
        #if i divides the given number
        if (nbr % i == 0):
            return False
    #if no factor found        
    return True        


#----- Greatest Common Divisor -----
# returns the greatest common divisor of two numbers recursively
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


#----- Inverse Modulo N -----
def inv(nbr, mod):
    # first reduce to least non-negative representative
    nbr = nbr % mod 
    #check gcd first
    if gcd(nbr, mod) > 1:
        print("This number is not invertible in this modulus.")
        return
    # create a list containing an arbitrary 1st element (0 in this case, but it doesn't matter)
    quotients = [0]

    #inner function, modified gcd that keeps track of quotients at each step
    def gcd2(a, b):
        if b == 0:
            return
        # append quotient to the list    
        quotients.append(a // b)    
        # recursion
        return gcd2(b, a % b)

    #builds quotient list    
    gcd2(mod, nbr)
    #create 2nd list holding EEA
    eea = [0, 1]
    # build eea list
    for i in range(1, len(quotients) - 1):
        eea.append(eea[i-1] - quotients[i] * eea[i])
    #store result
    inv = eea[-1]
    # make sure it is non negative
    while inv < 1:
        inv+= mod
    return inv, quotients, eea
