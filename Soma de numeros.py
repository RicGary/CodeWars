"""
Given two integers a and b, which can be positive or negative,
 find the sum of all the integers between and including them and
 return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples:

get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

        ===>>> min(a,b) pega o menor valor. <<<===
        ===>>> max(a,b) pega o maior valor. <<<===
"""

# Primeira tentativa

def get_sum(a,b):
    if b >= a:
       summ = sum(range(a, b + 1))
    if a >= b:
       summ = sum(range(b, a + 1))

    return summ

get_sum(-1, 2)

# Segunda tentativa com ajuda

def get_sum(a,b):
    return sum(range(min(a,b),max(a,b)+1))

print(get_sum(-1, 2))