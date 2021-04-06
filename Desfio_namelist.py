"""

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

"""


# Resolução

def namelist(names):

    str = ''

    lista = []

    for i in range(len(names)):
        lista.append(names[i]['name'])

    nomes = []
    if len(lista) > 0:
        for i in range(0 , len(names) - 1):
            nomes.append(lista[i])
        str = ', '.join(nomes)
        str+= ' & ' + lista[-1] if str != '' else lista[-1]

    return str

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))




