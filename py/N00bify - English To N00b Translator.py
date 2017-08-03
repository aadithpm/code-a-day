"""
https://www.codewars.com/kata/552ec968fcd1975e8100005a
"""
import re

noobz = {"too?":"2","fore?":"4","oo":"00","be":'b',"are":'r',"you":'u',
"please":"plz","people":"ppl","really":"rly","have":"haz","know":"no",
"s":"z","[\.,']":"","T00":"2"}

def n00bify(text):
    for noob in noobz:
        text = re.sub(noob,noobz[noob],text,flags=re.I)
    if text.split(" ")[0][0] in 'Ww':
        text = "LOL " + text
    if len(text.replace("!","")) >= 32:
        if text[0:3] == "LOL":
            text = text.replace("LOL","LOL OMG")
        else:
            text = "OMG "+ text
    text = " ".join(w.upper() if i % 2 != 0 else w for i,w in enumerate(text.split(" ")))
    text = re.sub("(\?|!)", "\g<1>" * len(text.split()), text).replace("!!", "!1")
    if text.split(" ")[0][0] in ['H','h']:
        text = text.upper()
    return text
