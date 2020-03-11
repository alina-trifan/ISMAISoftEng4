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


def loadClients ():
    ...


def printClients(v):
    ...
        
def saveEntries(l):
    ...
        
def addParkEntry():
   ...
    

def validPlate(s):
	match = re.search(r"[0-9]{2}[-][a-zA-Z]{2}[-][0-9]{2}", string)  
    	return False if match == None\
        	else ()

	
def matches(s, pattern):
    ...
    
    
def printClientPlates(c):
	clientes = []
    	for carro in vehicle:
		if carro[2] not in clientes:
	    	clientes.append(carro[2])
    	for cliente in clientes:
		matriculas = []
		for x in range(0, len(vehicle)):
	    		if (cliente == vehicle[x][2] ):
			matriculas.append(vehicle[x][0])        
		print(cliente, ": ", matriculas, "") 



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
