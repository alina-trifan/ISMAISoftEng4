
import csv
import operator
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
    print("Não existe nehum registo")
    lista = vehicles
    lista.sort(key=operator.itemgetter(2))
    for row in lista:
        print(f'{row[2]} : ({row[0]}, {row[1]})')
def saveEntries(l):
    ...
        
def addParkEntry():
    ...
def validPlate(s):
    ...

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

