import csv
import operator
from a import reader


def ordenar():

    sort = sorted(reader, key=operator.itemgetter(2,0))
      
    for eachline in sort :
        
        print (eachline[2]+" : ('"+eachline[0]+"'), '"+eachline[1]+"')")

ordenar()

