"""
There is an array of strings. All strings contains similar letters
except one. Try to find it!

Examples:
    find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
    find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces
 symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.
"""
def find_uniq(str):
    palavras = str
    tupla_original = tuple(sorted(''.join(set(x.lower())) for x in palavras))
    tupla_teste = tuple(reversed(tupla_original))

    for i in range(2):
        if not tupla_teste[i] == tupla_original[0] and not tupla_teste[i] == tupla_original[1]:
            print(palavras[tupla_original.index(tupla_teste[i])])
            return palavras[tupla_original.index(tupla_teste[i])]
        if not tupla_original[i] == tupla_teste[0] and not tupla_original[i] == tupla_teste[1]:
            print(palavras[tupla_teste.index(tupla_original[i])])
            return palavras[tupla_teste.index(tupla_original[i])]

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])