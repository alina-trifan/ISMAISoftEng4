import csv
import operator

def printClients(v):
    sort = sorted(vehicles,key=operator.itemgetter(2))
    for linha in sort:
        print(f'\t{linha[2]} : ({linha[0]}, {linha[1]})')
