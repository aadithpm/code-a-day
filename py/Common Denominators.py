"""
https://www.codewars.com/kata/54d7660d2daf68c619000d95
"""
from functools import reduce
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a,b):
    return a * b // gcd(a,b)
    
def convertFracts(lst):
    nums = [i[0] for i in lst]
    denoms = [i[1] for i in lst]
    _lcm = reduce(lcm,denoms)
    mult = [_lcm//i for i in denoms]
    return [[i*m,_lcm] for i,m in zip(nums,mult)]
