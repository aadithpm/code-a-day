"""
https://www.codewars.com/kata/maximum-subarray-sum/python
"""
def maxSequence(arr):
    if len(arr) == 0:
        return 0
    #Kadene's Algorithm for maximum subarray
    max_1 = max_2 = arr[0]
    for i in arr[1:]:
        max_1 = max(i, max_1 + i)
        max_2 = max(max_2, max_1)
    return max_2
