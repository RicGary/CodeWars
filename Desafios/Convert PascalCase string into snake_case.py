"""
Complete the function/method so that it takes a PascalCase string and
returns the string in snake_case notation. Lowercase characters can be
numbers. If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
"""


def to_underscore2(string):
    word = []
    string = str(string)
    for i in string[::-1]:
        word.append(i.lower())
        if i == i.upper() and i not in '0123456789':
            word.append('_')

    if '_' == word[-1]:
        word = word[0:len(word)-1]

    return ''.join(word)[::-1]


print(to_underscore2(1))


