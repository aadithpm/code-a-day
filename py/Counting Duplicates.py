"""
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
"""
def duplicate_count(text):
    text = text.lower()
    letters = set(text)
    co = 0
    for i in letters:
        co = co + 1 if text.count(i) > 1 else co
    return co
        
