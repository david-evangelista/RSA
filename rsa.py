# INSE 6110, F-2021
# Programming Project 
# David Evangelista
#   RSA: main function

from enc_dec import rsa_array_nbrs, rsa_str

def main():

    print("\nWelcome to my RSA Program!")

    #Generated primes
    p = 64621 #0xfc6d
    q = 61583 #0xf08f
    n = 3979555043
    phi_n = 3979428840
    e = 29033
    d = 1605039497


    # ---- Encrypting my message to send to my partner
    print("\nConversion of the message that I sent to my partner \"Cryptography\":")
    rsa_str(1805805343, 65537, "Cryptography")

    # ---- Received numbers from my partner
    partner_msg = ['2211766802','2907171786','2345409079','231146831','653177936','3361724814','2041627817',
                '3311288860','19475825','2625930274','2591958996','3465113968','1125923304']
    print("\nMy partner's numbers that I received were:")
    print(partner_msg)
    rsa_array_nbrs(n, d, partner_msg)
  
    # Signing my name using my n, and d
    print("\nSigning my name using my n, and d")
    name = "David Evangelista"
    rsa_str(3979555043, 1605039497, name)

    # Verifiying that my partner will use my public key and get my name
    print("\nVerifying that my partner will use my public key and get my name:")
    array = ['3924628909', '2483545029', '768440410', '3121037108', '3659078980', '3931968110']
    rsa_array_nbrs(3979555043, 29033, array)

    # Verifiying my partner's signature
    partner_sig = ['893824565', '1620196555', '1172275538', '1801182764', '1054725024']
    print("\nVerifiying my partner's signature, it should match \"Akshay Divakar\"")
    print("\nMy partner's numbers that I received were:")
    print(partner_sig)
    rsa_array_nbrs(1805805343, 65537, partner_sig)


    print("\nClosing program now, goodbye!")


if __name__ == "__main__":
    main()
