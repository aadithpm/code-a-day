"""
https://www.codewars.com/kata/51c8e37cee245da6b40000bd
"""
import re
def solution(string,markers):
    words = [i for i in string.split("\n")]
    for marker in markers:
        reg = re.compile(r"\s*\{}(.*)".format(marker))
        for i, word in enumerate(words):
            word = re.sub(reg, "", word)
            words[i] = word
    return '\n'.join(words)
