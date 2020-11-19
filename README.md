# RSA-encryption-Algorithm
2017325_1_a.py is the implementation of RSA encryption.
Input: p, q, m - in each line; p<q.
Output: c, e, d, n - each number in a separate line
Constraints: integers p, q and m are up to 1023 digits long. Avoid using loops.

2017325_1_b.py is the decryption mechanism.
Input: c, d, n - in each line.
Output: m
Constraints: same as 1.a.
Note: Values of m, c, d, n will be taken from 1.a. for evaluation.

# Calculation of the value of e, and how it will always remain coprime to φ.
e = gmpy2.next_prime(q)
This method to calculate ‘e’ will always return a coprime, let’s see how.
To Prove – e is coprime to Φ.
‘e’ is already prime due to the gmpy2.next_prime() function.
We know that factors of Φ are (p-1) and (q-1).
We know that p<q and q<e. So, neither of the factors of Φ can completely divide e. Now if the
factors of Φ can’t divide e, even Φ can’t. Meaning that GCD (e, Φ) = 1.
Example: -
Let (p-1) and (q-1) be 2 and 4. So here, p = 3 and q = 5.
Φ = 8
e = gmpy2.next_prime(q) = gmpy2.next_prime(5) = 7
So, e is neither divisible by 2 nor 4, and not even by Φ.
Proving that GCD (e, Φ) = 1.
