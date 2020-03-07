import csv
#Importação dos ficheiros de classes
from cliente import Cliente
from veiculo import Veiculo

#Variavel para guardar entradas
contadorEntradas = 0

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
    global contadorEntradas
    contadorEntradas = 0
    listaClienteVeiculo = []
    with open('ep1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter = ';')
        for row in reader:
            l_cliente = Cliente(row[2])
            l_cliente.removerTodosVeiculo()
            if not listaClienteVeiculo:
                l_cliente.adicionarVeiculo(row[0], row[1])
                listaClienteVeiculo.append(l_cliente)
                contadorEntradas += 1
            else:
                if l_cliente in listaClienteVeiculo:
                    l_veiculo = Veiculo(row[0], row[1])
                    for i in range(len(listaClienteVeiculo)):
                        if listaClienteVeiculo[i] == l_cliente and listaClienteVeiculo[i].verificarVeiculo(l_veiculo) == False:
                            listaClienteVeiculo[i].adicionarVeiculo(row[0], row[1])
                            listaClienteVeiculo[i].ordenarVeiculos()
                            contadorEntradas += 1
                else:
                    l_cliente.adicionarVeiculo(row[0], row[1])
                    listaClienteVeiculo.append(l_cliente)
                    contadorEntradas += 1
        return listaClienteVeiculo

def printClients(l_listaVeiculosCliente):
    l_listaVeiculosCliente = sorted(l_listaVeiculosCliente, key=lambda cliente: cliente.getNif()).copy()
    for i in range(len(l_listaVeiculosCliente)):
        print('\n'+str(l_listaVeiculosCliente[i])+'\n')
        print('     Matrícula  Marca')
        for index in range(l_listaVeiculosCliente[i].numeroVeiculos()):
            print('     '+str(l_listaVeiculosCliente[i].getVeiculoIndex(index)))

def saveEntries(l):
    ...

def addParkEntry():
   ...


def validPlate(s):
	...

def matches(s, pattern):
    ...


def printClientPlates(l_listaVeiculosCliente):
    l_listaVeiculosCliente = sorted(l_listaVeiculosCliente, key=lambda cliente: cliente.getNif()).copy()
    for i in range(len(l_listaVeiculosCliente)):
        print('\n'+str(l_listaVeiculosCliente[i])+'\n')
        print('     Matrículas:')
        for index in range(l_listaVeiculosCliente[i].numeroVeiculos()):
            print('     '+str(l_listaVeiculosCliente[i].getVeiculoIndex(index).getMatricula()))


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
        print('Nome do ficheiro: ep1.csv')
        print('Foram importados ' +str(contadorEntradas)+ ' registos.')

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
