"""
http://www.codewars.com/kata/mongodb-objectid/python
"""
from datetime import datetime

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        return isinstance(s,str) and all(c in '0123456789abcdef' for c in s) and len(s) == 24

    @classmethod
    def get_timestamp(cls, s):
        if cls.is_valid(s):
            return datetime.fromtimestamp(int(s[:8],base=16))
        else:
            return False
