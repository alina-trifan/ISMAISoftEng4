def addParkEntry():
    print("Qual o seu NIF?")
    print("Insira a matrícula:")
    matricula = input()
    while(validPlate(matricula) != True):
        print("Matrícula Inválida, as matrículas têm de ter um formato 00-XX-00, insira novamente:")
        matricula = input()
        
    entrada.append(matricula)   
    print("Insira a duração:")
    tempo = int(input())
    while(tempo<=0):
        print("Valor inválido, insira novamente:")
        tempo = int(input())
    entrada.append(tempo)
    return(entrada)
