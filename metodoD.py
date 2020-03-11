
  

def validPlate():

     plate_format = bool(re.search('[0-9]{2}[-][A-Z]{2}[-][0-9]{2}', s))
    return plate_format
    
validPlate()
