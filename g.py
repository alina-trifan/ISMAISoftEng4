import csv
import operator
carros = []
parque = []
nif = ""
i = True
custo = 0.0
file = 'ep1.csv'
openFile = open(file)
reader = csv.reader(openFile, delimiter=';')

def importar():
    
    for col in reader:
        
        carros.append(col)

    return carros
   


def importarD():
    file = 'parque.csv'
    openFile = open(file)
    reader = csv.reader(openFile, delimiter=';')
    for col in reader:
        
        parque.append(col)
    return parque

def gerarFatura(nif,lista,parque,i):
    while True:
        nif = input("Insira o nif: ")
        if len(nif) == 9 and nif.isdigit():
            print("NIF válido!")
            break
        else:
            print("NIF inválido!")
    print("NIF: ",nif)
    print("Fatura NIF:", nif)
    print("Matricula \t  Marca  \t Duração Custo")
    for linha in lista:
        for valor in linha:
            if valor == nif:
                for col in parque:
                    if linha[0] == col[0]:
                        custo = int(col[1]) * 0.01
                        
                        print(linha[0],"\t ",linha[1]," \t ",col[1],"\t ",custo)
                        i = False
    if i== True:
        print("Não existe")
        
            
            
        
importar()
parque = importarD()
gerarFatura(nif, carros,parque,i)

