def loadClients ():
    contador=0
    l = []
    Lista = open('ep1.csv')
    Ficheiro = csv.reader(Lista, delimiter=';')
    for linha in Ficheiro:
        l.append(linha) 
        contador +=1
    return l
