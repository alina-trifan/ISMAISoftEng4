def printClientPlates(c):
    clientes=[]
    for i in range(0,len(vehicles)):
        clientes.append(vehicles[i][2])
    clientes.sort()
    clientes = list(dict.fromkeys(clientes))
    for i in range(0,len(clientes)):
        matriculas=[]
        for l in range(0,len(vehicles)):
            if(clientes[i]==vehicles[l][2]):
                matriculas.append(vehicles[l][0])
        print("nif:",clientes[i],"matriculas:",matriculas)


    




