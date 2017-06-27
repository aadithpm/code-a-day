"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

http://mathworld.wolfram.com/Factorial.html

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)

Be careful 1000! has length of 2568 digital numbers.

"""
import math
multiples = [5,25,125,625,3125,15625,78125,390625,1953125,9765625,48828125,244140625]
def zeros(n):
    return sum(math.floor(n/i) for i in multiples)
