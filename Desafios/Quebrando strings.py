"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

# Primeira tentativa

"""
def solution(s):
    s = list(s)
    lista = []
    k = 0
    j = 2
    for i in range(int(len(s)/2)):
        lista.append(''.join(s[k:j]))
        k += 2
        j += 2
    if len(s) % 2 != 0:
        lista.append(''.join(((s[-1],'_'))))
    print(lista)
    return lista

solution('abcdef')
solution('abc')
"""

# Tentativa com ajuda

def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0 ,len(s), 2):
        result.append(s[i:i+2])
    print(result)
    return result

solution('abcdef')
solution('abc')

