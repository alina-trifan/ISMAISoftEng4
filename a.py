import csv
import operator

def loadClients():
    with open('ep1.csv') as ficheiro_csv:
        leitor = csv.reader (ficheiro_csv, delimiter=';')
        contador = 0
        vehicle=[]
        for linha in leitor:
            contador += 1
            vehicle.append(linha)
        print(f'Nome do ficheiro: ep1.csv')
        print(f'Foram importados {contador} registos.')
        return vehicle
