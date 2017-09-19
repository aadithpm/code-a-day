"""
https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""
def format_duration(seconds):
    if seconds == 0:
        return "now"
    h, m, s, d, y = None, None, None, None, None
    s = seconds % 60 
    m = seconds // 60 if seconds > 60 else None
    h = seconds // 3600 if m else None
    m = m % 60 if m else None
    d = seconds // 86400 if h else None
    h = h % 24 if h else None
    y = seconds // 31536000 if d else None
    d = d % 365 if d else None
    s = s if s != 0 else None
    if h:
        h = str(h) + " hour" if h == 1 else str(h) + " hours"
    if m:
        m = str(m) + " minute" if m == 1 else str(m) + " minutes"
    if s:
        s = str(s) + " second" if s == 1 else str(s) + " seconds"
    if d:
        d = str(d) + " day" if d == 1 else str(d) + " days"
    if y:
        y = str(y) + " year" if y == 1 else str(y) + " years"
    words = list(filter(lambda x: x, [y, d, h, m, s]))
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return words[0] + " and " + words[1]
    words = ', '.join(words[:len(words) - 1]) + " and " + words[len(words) - 1]
    return words  
