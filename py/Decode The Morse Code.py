"""
https://www.codewars.com/kata/decode-the-morse-code/python
"""
import re
def decodeMorse(morseCode):
    return re.sub("_+"," ",''.join([MORSE_CODE[i] if i in MORSE_CODE else "_" for i in morseCode.split(" ")])).lstrip().rstrip()
