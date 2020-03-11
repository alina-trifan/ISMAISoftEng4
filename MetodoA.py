def a():
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
    
a()
