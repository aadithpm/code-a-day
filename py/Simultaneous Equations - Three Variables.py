"""
http://www.codewars.com/kata/simultaneous-equations-three-variables/python
"""
import itertools
import numpy
import math
def solve_eq(eq):
    # your code here
    eq = list(itertools.chain(*eq))
    cnsts = [eq[3],eq[7],eq[11]]
    del eq[3],eq[6],eq[9]
    #
    a = numpy.array([eq[:3],eq[3:6],eq[6:9]])
    b = numpy.array(cnsts)
    return [round(i) for i in numpy.linalg.solve(a,b)]
