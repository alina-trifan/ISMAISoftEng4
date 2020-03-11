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
    print("Nome do Ficheiro: ep1.csv")

    #Descobrir numero de linhas no ficheiro
    f = open("ep1.csv", "r")
    linhas = len(f.readlines())
    print("Foram importados",linhas,"registos\n")
    f.close()

    #Guardar linhas numa lista
    f = open("ep1.csv", "r")
    lista = []
    i = 1
    while(i <= linhas):
        frase = f.read()
        lista.append(frase)
        i += 1
    f.close()

def printClients(v):
    sort = sorted(vehicles,key=operator.itemgetter(2))
    for row in sort:
        print(f'\t{row[2]} : ({row[0]}, {row[1]})')

def saveEntries(l):
    count = len(operations)
    with open('parque.csv',newline='',delimiter=";") as file:
        writer_csv = csv.writer(file)
        for i in range(0, count):
            writer_csv.writerow(operations[i])
    return writer_csv

def addParkEntry():
    matricula = ""
    i = 0

    duracao = ""
    j = 0

    info = []

    #verificar matricula
    while i != 1:
        matricula = input('Introduza a matricula, no formato 00-AA-00: ')
        if validPlate(matricula) == None:
            print('Matricula inválida!\n')
        else:
            info.append(matricula)
            i +=1

    #verificar valor da duracao
    while j != 1:
        duracao = input('Introduza a duração, em minutos: ')
        if duracao.isdigit() and int(duracao) > 0:
            info.append(duracao)
            j += 1
        else:
            print('Valor inválido!\n')

    #ler lista com as infos inseridas
    print('Informações: ', info)
    #sair do programa
    key = input('\nPressione enter para sair.')
    return info
    quit()


def validPlate(s):
    formato = re.search('[0-9]{2}[-][A-Z]{2}[-][0-9]{2}$', s)
    return None if formato == None\
        else ()

def matches(s, pattern):
    ...

def printClientPlates():
    #Descobrir numero de linhas no ficheiro
    f = open("ep1.csv", "r")
    linhas = len(f.readlines())
    f.close()

    if(linhas == 0):
        print("Sem clientes!")

    #Guardar linhas numa lista
    f = open("ep1.csv", "r")
    lista = []
    i = 1
    while(i <= linhas):
        frase = f.readline()
        lista.append(frase)
        i += 1

    #Separar com split
    x = 0
    r = 0
    nifs = []
    while(x < linhas):
        #fr é a string
        fr = lista[x]

        #Para guardar as separacoes em cada var
        matricula,marca,nif = fr.split(";")
        nif.replace(" ","")
        #print(nif.replace(" ",""))
        nifs.append(nif)
        y = 0
        soma = 0
        '''
        Em cima separo os dados que nos sao fornecidos e guardo os nifs todos
        num vetor, depois cada nif a medida q vai sendo usado e adicionado e
        no while asseguir vai ser comparado no vetor ou seja se ele tiver la
        presente significa q ja foi usado ou seja e repetido entao
        uso o continue para o mandar po inicio do primeiro while
        fazendo assim com que os nifs iguais nao sejam imitidos
        '''
        while(y < len(nifs)):
            if(nif == nifs[y]):
                soma += 1
            y += 1
        if(soma != 1):
            x += 1
            continue

        #Comparaçao nifs
        r = 0
        igual = ""
        while(r < linhas):
            lr = lista[r]

            #Para guardar as separacoes em cada var
            matricula2,marca2,nif2 = lr.split(";")

            if(nif == nif2):
                igual =  igual + matricula2 + " " + ";" + " "
                nif3 = nif2
            r += 1
        print("NIF:",nif3)
        print("Matricula:",igual,"\n")
        x += 1
    f.close()


def invoice(c, o):
    i = 0
    preco = 0
    infoVehicles = loadClients()
    #assumindo uma duracao de 20mins
    duracao = 20

    #verificar se nif é valor positivo
    while i != 1:
        nif = input('Introduza o seu NIF: ')
        if nif.isdigit() and int(nif) > 0:
            i += 1
        else:
            print('Valor inválido!\n')

    preco = (duracao * 0.01)

    print('\nMatricula Marca Duracao Custo')
    #verificar se NIF existe nos dados de entrada associados a matriculas
    #assumindo uma duracao de 20mins
    for row in infoVehicles:
        for item in row:
            if item == nif:
                print(row[0],'', row[1],'  ' ,duracao, ' ', preco)
    #verificar qual a duracao do veiculo

    #sair do programa
    key = input('\nPressione enter para sair.')
    quit()


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
