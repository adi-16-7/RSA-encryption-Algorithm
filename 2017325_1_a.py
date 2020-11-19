# Aditya Gupta
# 2017325
# Q1(a)

import gmpy2 
from gmpy2 import mpz
import random
import sympy # pip install sympy

def Greatest_Common_Divisor(A, B):
    gvd = gmpy2.gcd(A,B)
    return gvd

def Multi_Inverse(e, Fi):
    return sympy.mod_inverse(e, Fi)

def Check_If_Prime(N):
    a = gmpy2.is_prime(N)
    return(a)

def Generate_Pair(P, Q):
    if P==Q:
        raise ValueError("P and Q cant be equal.")
    elif (Check_If_Prime(P) == False and Check_If_Prime(Q) == False):
        raise ValueError("Error: p and q, both must be prime.")

    N = gmpy2.mul(P, Q)
    Fi = gmpy2.mul((P-1), (Q-1))
    e = gmpy2.next_prime(q)
    d = Multi_Inverse(e, Fi)
    return ((e,N),(d,N))

def Encryption(publicKey, message):
    e, N = publicKey 
    c = gmpy2.powmod(message, e, N)
    return c, e

if __name__ == "__main__":
    p = int(input("p : "))
    q = int(input("q : "))
    m = int(input("m : "))

    # 182302015849
    # 156702016043
    A, B = Generate_Pair(p, q)
    public_key = A
    private_key = B

    c, e = Encryption(public_key, m)
    d, N = private_key

    print(c)
    print(e)
    print(d)
    print(N)
    
    
 # 9352948374974159081733
#182302015927
#4252488962800942372855
#28567093412241238265507

