'''
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.

range() é uma função que produz uma série de números.
Pode especificar quando a função começa e pára com o primeiro e segundo argumentos.

O map() é uma função que aceita dois argumentos:o primeiro argumento é uma função para
iterar e lidar com o segundo argumento, o segundo argumento da função é um iterável
ou uma colecção.

set() remove valores repetidos em uma lista.

       ====>>> chr(), que converte inteiros na sua contraparte ASCII. <<<====
          ====>>> ord(), converte a contraparte ASCII em inteiros. <<<====
'''

# Utilizando o módulo string.


import string

def is_pangram(s):
    s = s.lower()
    for letra in string.ascii_lowercase:
        if letra not in s:
            print('Não é um pangrama.')
            break
    else:
        print('É um pangrama.')

is_pangram('The quick, brown fox jumps over the lazy dog!')

# Utilizando range() e map().

def is_pangram(s):
    s = s.lower()
    alfabeto = [chr(i) for i in range(97, 123)]
    for letra in ''.join(alfabeto):
        if letra not in s:
            print('Não é um pangrama')
            return False
    print('É um pangrama.')
    return True

is_pangram('The quick, brown fox jumps over the lazy dog!')

# Utilizando range() e ord().

def Alfabeto():
    return [chr(i) for i in range(ord('a'),ord('z')+1)]
Alfabeto = ''.join(Alfabeto())

def is_pangram(s):
    s = s.lower()
    for letra in Alfabeto:
        if letra not in s:
            print('Não é um pangrama')
            return False
    print('É um pangrama.')
    return True
is_pangram('The quick, brown fox jumps over the lazy dog!')



