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
    lista = vehicles
    lista.sort(key=operator.itemgetter(2))
    for row in lista:
        print(f'{row[2]} : ({row[0]}, {row[1]})')
def saveEntries(l):
    ...
        
def addParkEntry():
    registos = []
    matricula = input("Matricula:")
    while(validPlate(matricula) != True):
        print("Matrícula inválida!!")
        matricula = input("Matricula:")
    registos.append(matricula)
    duracao = input("Duracao:")
    if duracao.isnumeric() and int(duracao) >= 1:
        registos.append(duracao)
    else:
        print("A duracao tem que ser superior a 1!")
        duracao = input("Duracao:")
        registos.append(duracao)
    print(f'Matricula registada:{matricula} Duracao:{duracao}')
    return(registos)
def validPlate(s):
    plate_format = bool(re.search('[0-9]{2}[-][A-Z]{2}[-][0-9]{2}', s))
    return plate_format
def matches(s, pattern):
    ...
    
    
def printClientPlates(c):
    ...


def invoice(c, o):
     ...


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

