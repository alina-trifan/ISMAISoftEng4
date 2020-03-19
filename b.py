def printClients(l):
    ordenar = sorted(vehicle,key=operator.itemgetter(2))
    for linha in ordenar:
        print(linha[2], ": (", linha[0], ",", linha[1], ")")

