"""
https://www.codewars.com/kata/5235c913397cbf2508000048
"""
class Calculator(object):
  def evaluate(self, string):
      if isinstance(eval(string),int):
          return eval(string)
      elif isinstance(eval(string),float):
          return round(eval(string),3)
