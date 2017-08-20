"""
https://www.codewars.com/kata/523f5d21c841566fde000009
"""
def array_diff(a, b):
    return list(filter(lambda x: x not in b,a))
