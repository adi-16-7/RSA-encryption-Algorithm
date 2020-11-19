# Aditya Gupta
# 2017325
# Q1(b)

import sympy # pip install sympy
import gmpy2
from gmpy2 import mpz
import random

def Decryption(d, N, encrypted_message):
    m = gmpy2.powmod(encrypted_message, d, N)
    return m

if __name__ == "__main__":
    C = int(input("C : "))
    d = int(input("d : "))
    N = int(input("N : "))

    m = Decryption(d, N, C)
    print(m)


# 1816784607105850408603
# 182302015927
# 4252488962800942372855
# 28567093412241238265507