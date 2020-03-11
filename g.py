import re
import csv
import operator

#funcao com dados de entrada dos carros
def loadClients():
    with open('ep1.csv') as csv_file:
        read = csv.reader (csv_file, delimiter=';')
        cont = 0
        vehicle=[]
        for row in read:
            cont += 1
            vehicle.append(row)
        print(f'Foram importados {cont} registos.')
        return vehicle

def invoice ():

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

# chamada da função
invoice()
