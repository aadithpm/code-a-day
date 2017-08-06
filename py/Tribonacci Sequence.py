"""
https://www.codewars.com/kata/556deca17c58da83c00002db
"""
def tribonacci_gen(signature):
    a, b, c = signature
    while True:
        yield a
        a, b, c = b, c, a + b + c

def tribonacci(signature,n):
    trib = tribonacci_gen(signature)
    numbers = []
    for i in range(n):
        numbers.append(next(trib))
    return numbers
