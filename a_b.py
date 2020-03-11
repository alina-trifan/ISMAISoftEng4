#Mostrar dados do ficheiro e contar linhas
import csv
import operator
vehicle=[]
contador=0
Lista = open('ep1.csv')
Ficheiro = csv.reader(Lista, delimiter=';')
for linha in Ficheiro:
    print(linha[2], ": (", linha[0], ",", linha[1], ")")
    vehicle.append(linha)
    contador +=1
print("Contador: ",contador)

#ordenar lista importada

#ordenar = sorted(vehicle,key=lambda linha: linha[2])
ordenar = sorted(vehicle,key=operator.itemgetter(2))
for linha in ordenar:
    print(linha[2], ": (", linha[0], ",", linha[1], ")")


