"""
https://www.codewars.com/kata/simple-fraction-to-mixed-number-converter/python
"""
import fractions
import math
def mixed_fraction(s):
    numbers = [int(i) for i in s.split('/')]
    numbers = fractions.Fraction(numbers[0],numbers[1])
    if numbers.numerator > 0 and numbers.denominator > 0:
        quotient = str(int(math.floor(numbers)))
    else:
        quotient = str(int(math.ceil(numbers)))
    numbers = [numbers.numerator,numbers.denominator]
    remainder = str(int(math.fmod(numbers[0],numbers[1])))
    if remainder == "0":
        return quotient
    elif quotient == "0":
        return remainder + "/" + str(numbers[1])
    elif numbers[0] == 0:
        return "0"
    elif int(quotient) < 0 and int(remainder) < 0:
        return quotient + " " + str(abs(int(remainder))) + "/" + str(numbers[1])
    else:
        return quotient + " " + remainder + "/" + str(numbers[1])
