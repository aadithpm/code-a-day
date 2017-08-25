"""
https://www.codewars.com/kata/54d496788776e49e6b00052f
"""
from operator import itemgetter
def sieve(n):
    a = [True] * n
    a[0] = a[1] = False
    for i, prime in enumerate(a):
        if prime:
            yield i
            for j in range(i * i, n, i):
                a[j] = False
    
def sum_for_list(lst):
    sum_list = {}
    final_list = []
    if any( i < 0 for i in lst):
        dump = list(map(abs, lst))
        maxi = max(dump)
    else:
        maxi = max(lst)
    primes = sieve(maxi)
    primes = list(primes)
    for i in lst:
        for j in primes:
            if i % j == 0:
                if j in sum_list:
                    sum_list[j] += i
                else:
                    sum_list[j] = i
    for prime in sum_list:
        final_list.append([prime, sum_list[prime]])
    return sorted(final_list, key = itemgetter(0))
