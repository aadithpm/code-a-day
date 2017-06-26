"""
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'

"""

import re
def dashatize(num):
        if num is None or 0:
                return str(num)
        else:
                string = str(abs(num))
                string = list(map(lambda x: "-"+str(x)+"-" if int(x) % 2 != 0 else x,string))
                for i in range(0,len(string)):
                        if i == 0:
                                string[i] = re.sub("^-","",string[i])
                        if i == len(string)-1:
                                string[i] = re.sub("-$","",string[i])
                                
                string = "".join(string)
                return re.sub("--","-",string)
