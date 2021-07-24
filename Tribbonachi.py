"""
Well, you may have guessed it by now, but to be clear: you need to create a
 fibonacci function that given a signature array/list, returns the first n
  elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative
 number; if n == 0, then return an empty array (except in C return NULL)
  and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it
can be found in the Xbonacci kata.
"""

# Primeira tentativa

"""def tribonacci(signature, n):

    if n == 0:
        signature = []
        return signature
    if n == 1:
        signature.remove(signature[-1])
        signature.remove(signature[-1])
        return signature
    if n == 2:
        signature.remove(signature[-1])
        return signature

    for i in range(n-3):
        trib = signature[-1]+signature[-2]+signature[-3]
        signature.append(trib)
    return signature

tribonacci([300, 200, 100], 0)"""

# Segunda com ajuda do site

def tribonacci(signature, n):
    sig = signature[:n]
    for i in range(n-3):
        sig.append(sum(sig[-3:]))
    return sig

tribonacci([1, 1, 1], 10)