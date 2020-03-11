import csv

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
    with open('ep1.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=';')
      global lista
      lista = list(csv_reader)

      x=0
      for row in csv_reader:
          ++x

    csv_file.close()

    print("Nome do ficheiro: ep1.csv")
    print("Foram importados 6 registos.")
    return lista
    
      
def printClients(v):

    loadClients()
    
    lista.sort(key= lambda l: (l[2],l[0]))
    print(lista)
    
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
   ## op = menu(False)
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
