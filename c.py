import re
from a_b import vehicle

# imprimir matriculas por cliente [ 801401501 : ['00-AA-00'] ] -> não é preciso ser por ordem!

def printClientPlates(c):
    clientes = []

    # adicionar à lista clientes apenas nif's não repetidos
    for carro in vehicle:
        if carro[2] not in clientes:
            clientes.append(carro[2])


    for cliente in clientes:
        matriculas = []

        for x in range(0, len(vehicle)):

            if (cliente == vehicle[x][2] ):
                matriculas.append(vehicle[x][0])
        
        # imprimir matrículas por cliente - nif
        print(cliente, ": ", matriculas, "") 




