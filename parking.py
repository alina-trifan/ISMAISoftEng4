import csv
import operator
import re
import string
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
    with open('ep1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        contador = 0
        vehicles = []
        for row in reader:
            contador += 1
            vehicles.append(row)
        print(f'Nome do ficheiro: ep1.csv')
        print(vehicles)
        print(f'Foram importados {contador} registos.')
        return vehicles
    
def printClients(v):
    if not vehicles:
        print("Não há registos!")
    lista = vehicles
    lista.sort(key=operator.itemgetter(2))
    for row in lista:
        print(f'{row[2]} : ({row[0]}, {row[1]})')
        
def saveEntries(l):
    totalOperacoes = len(operations)
    with open('parque.csv','w',newline='') as file:
        file1 = csv.writer(file, delimiter=';')
        for i in range(0,totalOperacoes):
            file1.writerow(operations[i])
    print(f'Ficheiro gravado com sucesso!')
    return file1
        
def addParkEntry():
    matricula = input("Matricula:")
    matricula = matricula.upper()
    while(validPlate(matricula) != True):
        print("Matrícula inválida!!")
        matricula = input("Matricula:")
        matricula = matricula.upper()
    operations.append(matricula)
    duracao = input("Duracao:")
    if duracao.isnumeric() and int(duracao) >= 1:
        operations.append(duracao)
    else:
        print("A duracao tem que ser superior a 1!")
        duracao = input("Duracao:")
        operations.append(duracao)
    print(f'\nMatricula registada:{matricula}\nDuracao:{duracao} minutos')
    return(operations)

def validPlate(s):
    plate_format = bool(re.search('[0-9]{2}[-][A-Z]{2}[-][0-9]{2}', s))
    return plate_format

def matches(s, pattern):
    ...
       
def printClientPlates(c):
    clientes=[]
    for i in range(0,len(vehicles)):
        clientes.append(vehicles[i][2])
    clientes.sort()
    clientes = list(dict.fromkeys(clientes))
    for i in range(0,len(clientes)):
        matriculas=[]
        for l in range(0,len(vehicles)):
            if(clientes[i]==vehicles[l][2]):
                matriculas.append(vehicles[l][0])
        print("nif:",clientes[i],"matriculas:",matriculas)


def invoice(c, o):
    custoTotal = 0
    parque = []
    with open('ep1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            parque.append(row)
    while True:
        nif = input("NIF:")
        if len(nif) == 9:
            break
        else:
            print("NIF inválido!")
    print(f'Fatura NIF: {nif}')

    print('\nMatricula Marca Duracao Custo')
###############################################################################
vehicles = []
operations = []
op = menu(True)

while True:
    op = menu(False)
    if op == 0:
        print('Obrigado por usar o nosso software!')
        break
        
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

