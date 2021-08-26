"""
There is an array with some numbers. All numbers are equal except for one.
Try to find it!

Examples:
    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.

iteravel.count(valor) conta quantas vezes determinado elemento apareceu
"""

"""
def find_uniq(arr):
    array = sorted(arr)
    test = []

    if array[1] == array[0]:
        if array[1] != array[-1]:
            test.append(array[-1])
    test.append(array[0])

    n = test[0]
    return n

find_uniq([2, 2, 2, 2, 2, 10])
"""

# ou

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

find_uniq([2, 2, 2, 2, 2, 10])





