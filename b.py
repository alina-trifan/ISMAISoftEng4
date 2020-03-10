import csv
import operator

def printClients(v):
    clientes=[]
    if not vehicles:
        print("\nNão existem registos.")
    for i in range(0,len(vehicles)):
        clientes.append(vehicles[i][2])
    clientes.sort()
    clientes = list(dict.fromkeys(clientes))
    for i in range(0,len(clientes)):
        for a in range(0,len(vehicles)):
            if (clientes[i]==vehicles[a][2]):
                print("NIF:",clientes[i],"Matrícula:",vehicles[a][0],"Marca:",vehicles[a][1])
