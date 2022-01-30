# INSE 6110, F-2021
# Programming Project 
# David Evangelista
#   RSA: p, q, n, e generation

import random
from nbr_theory import is_prime, gcd, inv

#----- Number Generation -----

#----- N-Bit Pseudo-Random Prime -----
# generates an n-bit pseudo-random prime
def gen_prime(nbr_bits):
    #generate a random 16 bit number
    nbr = random.getrandbits(nbr_bits)
    #increment until it is prime
    while not (is_prime(nbr)):
        nbr+=1
    return nbr

#----- P & Q Generator -----
# generates p and q 16-bit primes to use for RSA
def gen_pq16():
    print("\nGenerating p, q...")
    p = gen_prime(16)
    q = gen_prime(16)
    #if twin primes, print warning
    if abs(p - q) == 2:
        print("\nWarning. Twin primes.")
    print("\nGenerated prime p: "+ str(p)+" = "+ hex(p)[:-1])
    print("Generated prime q: "+ str(q)+" = "+ hex(q)[:-1])     
    return p, q

#----- E & D Generator -----
def gen_ed16(phi_n):
    e = random.getrandbits(16)
    #if gcd != 1, increment until it does
    while gcd(e, phi_n) > 1:
        e += 1
    d = inv(e, phi_n) 
    print("Generating number coprime to phi(n): e = "+str(e)+"\nand the inverse of e mod phi(n):    d = "+str(d)+"\n")       
    return e, d 

#----- N & Euler-Totient -----
def n_totient(p, q):
    if not is_prime(p) or not is_prime(q):
        print("\nError, you must provide two prime numbers.")
        return
    n = p * q
    phi_n = (p-1) * (q-1)
    print("Therefore, n = p * q = "+str(n)+" and phi(n) = "+str(phi_n))    
    return n, phi_n
