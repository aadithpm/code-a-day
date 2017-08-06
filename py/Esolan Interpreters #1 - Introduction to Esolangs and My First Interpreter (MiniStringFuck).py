"""
https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0
"""
import re
def my_first_interpreter(code):
    #Remove all non command characters
    code = re.sub(r'[^+.]','',code)
    #'Pointer' points to 0
    ptr = 0
    #Split up commands from code
    incs = [i for i in code.split('.')]
    output = []
    for i in incs: #For each command/increment operation in the code
        ptr += len(i) #Add the length of the command i.e amount by which to increment the pointer
        if ptr > 127: #If pointer crosses 256,
            ptr = ptr % 128 #Handles overflow smoothly. Example: 118 + 12 is now 2. 118 + 240 is now 2 as well
        output.append(chr(ptr)) #Add each character to the output
    return ''.join(output[:len(output)-1]) #For some weird-ass reason, the last character gets added twice, so discard that and return
