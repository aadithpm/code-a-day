"""
https://www.codewars.com/kata/coordinates-validator/python
"""
import math
def is_valid_coordinates(coordinates):
    try:
        coordinates = coordinates.replace(", ",",")
        coords = [math.floor(float(i)) for i in coordinates.split(',')]
        return not re.search(r"[A-Za-z\s]",coordinates) and coords[0] in range(-90,91) and coords[1] in range(-181,181) and coordinates.count(",") == 1
    except ValueError:
        return False
