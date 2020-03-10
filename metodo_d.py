import re

def validPlate(s):
    x = bool(re.search("[0-9]{2}-[A-Z]{2}-[0-9]{2}", s))
    return x;
