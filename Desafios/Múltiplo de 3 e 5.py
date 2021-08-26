"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
Also, if a number is negative, return 0(for languages that do have them)
"""

# Primeira tentativa

"""
def solution(number):

    if number < 0:
        print(0)
        return 0

    lista = list(range(1,number))
    lista_temporaria = []

    for i in lista:
        if i % 3 == 0:
            lista_temporaria.append(i)
    for i in lista:
        if i % 5 == 0:
            lista_temporaria.append(i)

    #print(f'A some é {sum(lista_temporaria)}, e os múltiplos são {lista_temporaria}')

    return sum(set(sorted(lista_temporaria)))
"""

# Forma 2 com ajuda

def solution(number):
    soma = 0
    if 0 > number:
        return 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            soma += i
    print(soma)
    return soma

solution(45)