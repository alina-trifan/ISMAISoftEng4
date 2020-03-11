import re
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


#funcao verificar formato da matricula
def validPlate(s):
    formato = re.search('[0-9]{2}[-][A-Z]{2}[-][0-9]{2}$', s)
    return None if formato == None\
        else ()


# chamada da função
addParkEntry()
