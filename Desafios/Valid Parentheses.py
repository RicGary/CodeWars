"""
Write a function that takes a string of parentheses, and determines if the order
of the parentheses is valid. The function should return true if the string is
valid, and false if it's invalid.

Examples:
    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid
ASCII characters. Furthermore, the input string may be empty and/or not contain
any parentheses at all. Do not treat other forms of brackets as parentheses
(e.g. [], {}, <>).


"""

# Forma 1


def valid_parentheses(string):
    from collections import Counter

    if type(string) == str:
        count = Counter(string)
        if count['('] != count[')']:
            return False
        string = list(string)

    for k, i in enumerate(string):
        for j in range(len(string) - 1):
            if i == ')':
                return False
            if i == '(' and string[j + 1] == ')':
                string[k] = 0
                string[j + 1] = 0

                valid_parentheses(string)

    count = Counter(string)
    if count['('] != count[')']:
        return False

    return True

# Forma 2


def valid_parentheses2(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

