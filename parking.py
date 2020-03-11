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


def loadClients ():
    with open('ep1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        vehicles = []
        contador = 0
        for row in reader:
            contador += 1
            vehicles.append(row)
        print(f'Nome do ficheiro: ep1.csv')
        print(f'Foram importados {contador} registos.')
        return vehicles

def printClients(v):
    ...
def saveEntries(l):
    ...
        
def addParkEntry():
   ...
    

def validPlate(s):
    from re import compile
    
    plate_format = compile('^[0-9]{2}[-][A-Z]{2}[-][0-9]{2}$')

    

    plates = ["00-AA-00", "00-ZZ-00", "11-AB-11", "99-XY-99", "99-XY-99", "50-UA-50"]

    for plate in plates:
        if plate_format.match(plate) is not None:
            print ("Correct plate")
        else:
            print ("Incorrect plate")

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
