"""
https://www.codewars.com/kata/simple-fun-number-166-best-match/python
"""
def best_match(goals1, goals2):
  goals = [[i - j, j] for i,j in zip(goals1,goals2)]
  _min = min([i[0] for i in goals])
  _max = max([i[1] for i in goals if i[0] == _min])
  return goals.index([_min,_max])