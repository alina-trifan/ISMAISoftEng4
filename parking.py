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
    import csv
    with open('ep1.csv', newline='') as csvfile:      
        reader = csv.reader(csvfile)
        data = list(reader)  
    return data 


def printClients(v):
    ...
        
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
    #op = menu(False)
    if op == 0:
        print('Obrigado por usar o nosso software!')
        break
        
    elif op == 1:
        vehicles += loadClients()    
        print("Clients List Loaded!")
        
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
    if op != 0:
        op = menu(True)