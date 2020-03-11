def addParkEntry():
    registos = []
    matricula = input("Matricula:")
    while(validPlate(matricula) != True):
        print("Matrícula inválida!!")
        matricula = input("Matricula:")
    registos.append(matricula)
    duracao = input("Duracao:")
    if duracao.isnumeric() and int(duracao) >= 1:
        registos.append(duracao)
    else:
        print("A duracao tem que ser superior a 1!")
        duracao = input("Duracao:")
        registos.append(duracao)
    print(f'Matricula registada:{matricula} Duracao:{duracao}')
    return(registos)
addParkEntry()
