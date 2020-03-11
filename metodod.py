
  

def validPlate():

    from re import compile

    plate_format = compile('^[0-9]{2}[-][A-Z]{2}[-][0-9]{2}$')

    

    for plate in vehicles:
        if plate_format.match(plate) is not None:
            return True
        else:
            return False

    
validPlate()
