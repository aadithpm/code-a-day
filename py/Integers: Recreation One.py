"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays(in C an array of Pair), each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]

The form of the examples may change according to the language, see Example Tests: for more details.

"""

"""
Author's Note: The chances of this code being accepted by the CodeWars compiler is slighty less as the timeout of 12000 ms by default has a good chance of firing depending on what random numbers are generated to test your code. An idea might be to utilise a cache that holds all the possible right values from 1 to say, 30000. However, I was able to do the same code in JS without any issues so I dropped it at this. Feel free to extend this into a completely working version.
"""

import math
def list_squared(m, n):
        return list(map(list,[(c+m,x) for c,x in enumerate([sum([j * j for j in range(1,i+1) if i % j == 0]) for i in range(m,n)]) if math.sqrt(x).is_integer()]))

