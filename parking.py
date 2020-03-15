import csv
import re
import pandas as pd

#Importação dos ficheiros de classes
from cliente import Cliente
from veiculo import Veiculo
from duracao import Duracao
from function import *
from ocupa import Ocupa
from fatura import Fatura

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
        print('7 - Remover Veiculo')
        print('8 - Registar entrada de Veiculo')
        print('9 - Registar saida de Veiculo')
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
            if len(str(row[2])) < 9 or str(row[2]).isnumeric() == False:
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

def removeVehicle(matricula):
    indexRemove = -1
    matricula = correctMatricula(str(matricula))
    vehicleExist = False
    with open('ep1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter = ';')
        for row in reader:
            if (str(row[0]) == matricula):
                print(indexRemove)
                vehicleExist = True
                break
            indexRemove += 1
    if (vehicleExist == False):
        print("Veiculo não encontrado.")
    else:
        with open('ep1.csv') as csv_file:
            pandaReader = pd.read_csv(csv_file, sep = ";")
            pandaReader.drop([indexRemove], inplace = True)
            pandaReader.to_csv("ep1.csv", index=False, sep = ';')

def printClients(l_listaVeiculosCliente):
    l_listaVeiculosCliente = sorted(l_listaVeiculosCliente, key=lambda cliente: cliente.getNif()).copy()
    for i in range(len(l_listaVeiculosCliente)):
        print('\n'+str(l_listaVeiculosCliente[i])+'\n')
        print('     Matrícula  Marca')
        for index in range(l_listaVeiculosCliente[i].numeroVeiculos()):
            print('     '+str(l_listaVeiculosCliente[i].getVeiculoIndex(index)))

def saveEntries(combine):

    print("combine", combine)
    with open ('parque.csv', mode='a', newline='') as parque_file:
        parque_writer = csv.writer(parque_file, delimiter=';')
        for x in range(0, len(combine)-1,2):
            parque_writer.writerow([combine[x]]+[str(combine[x+1])])
    print(("Ficheiro gravado com sucesso"))
    df = pd.read_csv('parque.csv', sep=';')
    df.sort_values(by=['duracao'], ascending=False, inplace=True)
    df.to_csv('parque.csv', sep=';', index=False)
    combine = []

def addParkEntry():
    global combine
    combine = []

    while True:
        m1, plateFlag = validPlate()
        if (m1!='0' and m1 !=''):
            while True:
                if plateFlag == True:
                    while True:
                        d1, durationFlag, exitFlag = Duracao.validDuration()
                        if durationFlag == True:
                            if exitFlag == 0:
                                combine.append(m1)
                                combine.append(d1)
                                print("combinex", combine)
                                m1, plateFlag = validPlate()
                        else:
                            plateFlag = False
                        break
                elif (m1=='0' or m1 ==''):
                    print("Obrigada por usar nosso software.")
                    break
                else:
                    print("Valor inválido")
                    m1, plateFlag = validPlate()
        break


def validPlate():

    model8 = re.compile('^\d{2}[-][A-Z]{2}[-]\d{2}$')
    model6 = re.compile('^\d{2}[A-Z]{2}\d{2}$')
    m = input("Digite a matricula (0 ou Enter para sair): ")
    m = m.upper();

    if len(m) == 8 and model8.match(m):
        print("Matricula: ", m)
        return m, True

    elif len(m) == 6 and model6.match(m):
        print("Valor necessita correção")
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


def invoice(nif):
    fatura = Fatura(Cliente(nif))
    fatura.calcularValor()
    print("NIF: "+nif)
    print("ID da Fatura: "+fatura.getId())
    print("")
    print("Matricula    Marca               Duracao     Custo")
    for ocupa in fatura.getOcupa():
        print(ocupa.getVeiculo().getMatricula()+"   "+ocupa.getVeiculo().getMarca()+"                 "+ocupa.getDuracao()+"        "+ocupa.getValor())
    print("Total:                                        "+fatura.getValorTotal())


def vehicleEntry():
    matricula = input("Introduza Matricula: ")
    marca = input("Introduza Marca: ")
    ocupa = Ocupa(Veiculo(matricula, marca))
    print("Veiculo de matricula "+ ocupa.getVeiculo().getMatricula()+" deu entrada ao parque.")
    ocupacoes
###############################################################################
vehicles = []
operations = []
ocupacoes= []
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
        nif = input("Introduza o seu NIF: ")
        invoice(nif)

    elif op == 7:
        matricula = input('Insira Matricula; ')
        removeVehicle(matricula)

    elif op == 8:
        vehicleEntry()

    elif op == 9:
        matricula = input('Insira Matricula: ')
        registerSaida(matricula)
