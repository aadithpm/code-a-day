"""
https://www.codewars.com/kata/55c6126177c9441a570000cc/solutions/python
"""
from operator import itemgetter
def digits(number):
    s = 0
    while number > 0:
        s += number % 10
        number = number / 10
    return s
    
def order_weight(strng):
    strng = [[i, digits(int(i))] for i in strng.split()]
    strng.sort(key = itemgetter(1, 0))
    return ' '.join([i[0] for i in strng])
