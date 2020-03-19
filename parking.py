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
    import csv
    file_name = 'ep1.csv'
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)      
    print("Nome do ficheiro: "+file_name)
    print("Foram importados "+str(len(data))+" registos")
    return data 


def printClients(v):
   s = sorted(v, key = lambda x: (x[2], x[1]))
   for client in s:
    print("Numero Contribuinte", client[2]+" : ('""Matricula : "+client[0]+"','" "Marca : "+client[1]+"')")
        
def saveEntries(l):
    ...

def pedirtempo():

    tempo= int(input('Qual o tempo que esteve estacionado no parque de estacionamento(Minutos)? '))

    
    while tempo<0:
        print ('Tem de ser um valor positivo')

        tempo= int(input('Qual o tempo que esteve estacionado no parque de estacionamento(Minutos)? '))

    return tempo

        
def addParkEntry():
    matricula= str(input('Qual a sua Matrícula? Ex:00-XX-00: ' ))

    if validPlate(matricula):
        tempo = pedirtempo()

        thisdict = {
            matricula : tempo
        }

        print (thisdict)
    else:
        print('Tem de introduzir uma matricula válida')
        
    
# d.	Escreva uma função que valide se uma string, passada como argumento, representa uma matrícula válida em Portugal. Considere apenas matrículas 
# posteriores a 2005 compostas por letras no meio como no seguinte exemplo: 00-AA-00. A função deverá devolver um valor lógico Verdadeiro se a matrícula for válida e Falso, caso contrário.
def validPlate(matricula):
    if re.findall("^(\d{2}-[A-Z]{2}-\d{2})$", matricula):
        return True
    else:
        return False

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
