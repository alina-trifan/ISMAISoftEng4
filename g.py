import re
import csv
import operator


def clientLoad():
    vehicle = []
    contador = 0
    Lista = open('ep1.csv')
    Ficheiro = csv.reader(Lista, delimiter=';')
    for linha in Ficheiro:
        print(linha[2], ": (", linha[0], ",", linha[1], ")")
        vehicle.append(linha)
        contador += 1
        return vehicle


def invoice():

    i = 0
    preco = 0
    infoClientes = clientLoad()
    duracao = int(input("Duracão: "))
    preco = duracao * 0.01

    while i < 0:
        nif = input('Introduza o seu NIF: ')
        if nif.isdigit() and int(nif) > 0:
            i += 1
        else:
            print('Valor inválido!\n')

    for row in infoVehicles:
        for item in row:
            if item == nif:
                print('\nMatricula Marca Duracao Custo')
                print(row[0], '', row[1], '  ', duracao, ' ', preco)


invoice()
