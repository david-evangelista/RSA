# INSE 6110, F-2021
# Programming Project 
# David Evangelista
#   RSA: number generation

from nbr_gen import gen_ed16, gen_pq16, n_totient

# generating primes p, q, (16 bits each)
p, q = gen_pq16()

# computing n, phi(n)
n, phi_n = n_totient(p, q)

#generating e s.t. gcd(e, phi(n)) == 1, finding d
e, d = gen_ed16(phi_n)
