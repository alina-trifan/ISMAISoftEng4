import csv
import operator
import re

def menu(text):
    print()
    print('Opcoes disponiveis:')
    if text:
        print('0 - Terminar')
        print('1 - Ler ficheiro de clientes')
        print('2 - Imprimir clientes ordenados')
        print('3 - Mostrar matriculas por Cliente')
        print('4 - Adicionar acesso ao parque')
        print('5 - Gravar acessos ao parque')
        print('6 - Gerar fatura para um cliente')
    else:
        print('[Impressao das varias opcoes]')
        
    o = int(input('Opcao? '))
    return o


def loadClients():
    file = 'ep1.csv'
    openFile = open(file)
    reader = csv.reader(openFile, delimiter=';')
    vehicles = []
    for col in reader: 
        vehicles.append(col)
    print("Nome do ficheiro: ", file)
    print("Foram importados", len(vehicles)," registos.")
    return vehicles 

def printClients(v):
    carros = vehicles
    carros.sort(key=operator.itemgetter(2,0))  
    for eachline in carros :
        print (eachline[2]+" : ('"+eachline[0]+"'), '"+eachline[1]+"')")
        
def saveEntries(l):
    if not operations:
        print("Não existem entradas no Parque!")

    else:
        with open ('parque.csv', 'a') as file:
            w = csv.writer(file, delimiter=';')
            w.writerow([operations[0],operations[1]])
            operations.remove(operations[1])
            operations.remove(operations[0])

        print("Foram adicionadas entradas no Parque!")
        
def addParkEntry():
    matriculaInserida = str(input("Introduza a matricula: "))
    matriculaInserida = matriculaInserida.upper()
    while (validPlate(matriculaInserida) != True):
        print("Matricula incorreta")
        matriculaInserida = str(input("Introduza a matricula: "))
        matriculaInserida = matriculaInserida.upper()
    operations.append(matriculaInserida)
    while True:
        try:
            duracao = int(input("Introduza a duração (em minutos): "))
            if duracao <= 0:
                print("Inserir um número inteiro positivo")
                continue
            return duracao
            break
        except:
            print("Inserir um número inteiro positivo")
def validPlate(s):
    formato_matricula = bool(re.search('^[0-9]{2}[-][A-Z]{2}[-][0-9]{2}', s))
    return formato_matricula


def matches(s, pattern):
    ...
    
    
def printClientPlates(c):
    clientes = []
    
    if not vehicles:
        print("Não existem clientes!")

    veiculos = len(vehicles)
     
    for x in range (veiculos):
        clientes.append(vehicles[x][2])

        
    clientes.sort()
    clientes = list(dict.fromkeys(clientes))
    
    
    for x in range(len(clientes)):
        
        matriculas = []
        
        for b in range(veiculos):
            
            if(clientes[x] == vehicles[b][2]):
                matriculas.append(vehicles[b][0])
                
                
        print("Contribuinte: ",clientes[x],"Matrículas: ",matriculas)


def invoice(c, o):
    custoTotal = 0
    i = True
    parque = []
    file = 'parque.csv'
    openFile = open(file)
    reader = csv.reader(openFile, delimiter=';')
    for col in reader:
        if col != []:
            parque.append(col)

    while True:
        nif = input("Insira o nif: ")
        if len(nif) == 9 and nif.isdigit():
            print("NIF válido!")
            break
        else:
            print("NIF inválido!")
    print("NIF: ",nif)
    print("Fatura NIF:", nif)
    if parque == []:
        print("Ficheiro vazio")
        i = False
    else:
        if c == []:
            print("Leia ficheiros dos clientes primeiro")
            i = False
        else:
            print("Matricula \t  Marca  \t Duração Custo")
            for linha in c:
                for valor in linha:
                    if valor == nif:
                        for col in parque:
                            if linha[0] == col[0]:
                                custo = int(col[1]) * 0.01
                                custoTotal += custo
                                print(linha[0],"\t ",linha[1]," \t ",col[1],"\t ",custo)
                                i = False
            print("Total: \t\t\t\t\t ",custoTotal)
    if i== True:
        print("Não existe")

###############################################################################
vehicles = []
operations = []
op = menu(True)

while True:
    op = menu(False)
    if op == 0:
        print('Obrigado por usar o nosso software!')
        break;
        
    elif op == 1:
        vehicles += loadClients()
        
    elif op == 2:
        printClients(vehicles)

    elif op == 3:
        printClientPlates(vehicles)
        
    elif op == 4:
        operations.append(addParkEntry())
    
    elif op == 5:
        saveEntries(operations)
        
    elif op == 6:
        invoice(vehicles, operations)
