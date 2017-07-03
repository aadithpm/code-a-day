"""
https://www.codewars.com/kata/help-your-granny/solutions/python/me/best_practice
"""
import math
def tour(friends, friend_towns, home_to_town_distances):
    d = 0
    last_d = 0
    friend_towns = [[friend,town] for friend,town in friend_towns if friend in friends]
    for f,t in friend_towns:
        if t in home_to_town_distances:
            _d = home_to_town_distances[t]
            if d == 0:
                d += _d
                last_d = _d
            else:
                d += math.sqrt(_d ** 2 - last_d ** 2)
                last_d = _d
    d += home_to_town_distances[t]
    return int(math.floor(d))
