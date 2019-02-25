"""
https://www.codewars.com/kata/consecutive-strings/python
"""
def longest_consec(strarr, k):
    if k < 1 or k > len(strarr) or len(strarr) == 0:
        return ''
    cur_len = 0
    cur_string = ""
    for idx, val in enumerate(strarr[:len(strarr) - k + 1]):
        temp_str = ''.join(strarr[idx: idx + k])
        if len(temp_str) > cur_len:
            cur_string = temp_str
            cur_len = len(temp_str)
    return cur_string