import csv
import re

#Importação dos ficheiros de classes
from cliente import Cliente
from veiculo import Veiculo
from duracao import Duracao

#Variavel para guardar entradas
contadorEntradas = 0
combine = 0

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
            if int(row[2]) < 0 or len(str(row[2])) < 9 or str(row[2]).isnumeric() == False:
                pass
            else:
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

def saveEntries(combine):

    with open ('parque.csv', mode='a', newline='') as parque_file:
        parque_writer = csv.writer(parque_file, delimiter=';')
        for x in range(0, len(combine)-1,2):
            parque_writer.writerow([combine[x]]+[str(combine[x+1])])
    print(("Ficheiro gravado com sucesso"))
    combine = []

def addParkEntry():
    global combine
    combine = []

    while True:
        m1, plateFlag = validPlate()
        if (m1!='0' and m1 !=''):
            while True:
                if plateFlag == True:
                    break
                else:
                    print("Valor inválido")
                    m1, plateFlag = validPlate()

            while True:
                d1, durationFlag, exitFlag = Duracao.validDuration()
                if durationFlag == True:
                    break
        else:
            break

        if exitFlag == 0:
            combine.append(m1)
            combine.append(d1)


def validPlate():


    model8 = re.compile('^\d{2}[-][A-Z]{2}[-]\d{2}$')
    model6 = re.compile('^\d{2}[A-Z]{2}\d{2}$')
    m = input("Digite a matricula (0 ou Enter para sair): ")
    m = m.upper();

    if len(m) == 8 and model8.match(m):
        print("Matricula: ", m)
        return m, True

    elif len(m) == 6 and model6.match(m):
        print("Valor inválido")
        correcao = list(m)
        m = (correcao[0]+correcao[1]+"-"+correcao[2]+correcao[3]+"-"+correcao[4]+correcao[5]);
        print("Correção: ", m)
        return m, True

    else:
        return m, False

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
    fatura = []

    custo = 0
    total = 0
    
    nif = int(input("Introduza o seu NIF: "))

    while nif < 0 or nif > 999999999:
        print("NIF inválido, introduza de novo!")
        nif = int(input("Introduza o seu NIF: "))
        
    if 0 < nif <= 999999999:
        fatura.insert(0, nif)

    custo = (0.01 * Duracao)
    
    fatura.insert(custo)
    

    print(fatura)
    

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
