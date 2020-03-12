def validPlate(s):
    import re
    matx = bool(re.search("^[0-9]{2}-[A-Z]{2}-[0-9]{2}", s))
    return matx;
