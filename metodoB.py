import csv
import operator

def printCliente():
    lista = vehicles
    lista.sort(key=operator.itemgetter(2))
    for row in lista:
        print(f'{row[2]} : ({row[0]}, {row[1]})')
