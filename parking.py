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
    contador=0
    l = []
    Lista = open('ep1.csv')
    Ficheiro = csv.reader(Lista, delimiter=';')
    for linha in Ficheiro:
        l.append(linha) 
        contador +=1
    return l


def printClients(v):
    print(l)
    ordenado = []
    ordenar = sorted(l,key=operator.itemgetter(2))
    #return ordenar
    for i in range(len(ordenar)):
        #print(v)
        print(l[2], ": (", l[0], ",", l[1], ")") 
        
def saveEntries(l):
    ...
        
def addParkEntry():
   duracao = ""
   matricula = ""
   i = 0 #contador para a duração
   p = 0 # contador para a matricula
   while p != 1:
       matricula = input("Introduza a matricula no formato 00-AA-00\n")
       if verifica_matricula(matricula) == False:
           print("Não introduziu uma matricula válida")
       else:
           p +=1 # validou a matricula e passa para o passo seguinte
   return matricula
   while i != 1:        
       duracao = input("Introduza a duração\n")
       if duracao.isdigit() and int(duracao) > 0:
           i += 1 #validou a duração e passa para o passo seguinte
       else:
           print("Não introduziu um numero válido")
   print(matricula," - ",duracao)
   return duracao
    
def validPlate(s):
	match = re.search(r"[0-9]{2}[-][a-zA-Z]{2}[-][0-9]{2}", string)  
    	return False if match == None\
        	else True

	
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
