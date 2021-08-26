"""
Write a function that takes in a string of one or more words,
 and returns the same string, but with all five or more letter
  words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:

spinWords("Hey fellow warriors") => "Hey wollef sroirraw"
spinWords("This is a test") => "This is a test"
spinWords("This is another test") => "This is rehtona test"
"""

# Minha primeira tentativa.

"""
def spin_words(string):
    frase = []
    lista = string.split()
    for palavra in lista:
        if len(palavra) >= 5:
            lista = list(palavra)
            lista.reverse()
            frase.append(''.join(lista))
        else:
            frase.append(palavra)

    print(' '.join(frase))
    return ' '.join(frase)

spin_words("This is another test")
"""

# Tentativa com ajuda do site.

def spin_words(string):
    frase = []
    lista = string.split()
    for palavra in lista:
        if len(palavra) >= 5:
            frase.append(palavra[::-1]) # Pega a palavra como se fosse uma lista
                                        # e inverte.
        else:
            frase.append(palavra)

    print(' '.join(frase))
    return ' '.join(frase)

spin_words("This is another test")
