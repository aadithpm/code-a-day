"""
https://www.codewars.com/kata/55983863da40caa2c900004e
"""
#Function to split a number into it's constituent digits
def digitize(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    return list(reversed(digits))

#Function to multiply the number by 10 based on it's place (unit digit, ten's digit, etc.)
def dedigitize(num):
    digits = [c * (10 ** i) for i,c in enumerate(reversed(num))]
    return sum(digits)
    
def next_bigger(n):
    digits = digitize(n)
    if len(digits) == 1:
        return -1
    if len(digits) == 2:
        if digits[1] > digits[0]:
            #Algorithm covers this possibility, but eh, had to code the else part, so..
            return digits[1] * 10 + digits[0]
        else:
            return -1
    try:
        #If empty sequence is encountered, means further generation of next bigger number is not possible
        i = max(i for i in range(1,len(digits)) if digits[i-1] < digits[i])
        j = max(j for j in range(i,len(digits)) if digits[j] > digits[i-1])
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = reversed(digits[i:])
        return dedigitize(digits)
    except:
        #Handling empty sequence exception
        return -1
