def printClientPlates(c):
    clientes=[]
    if not vehicles:
        print("\nNão existem clientes!")
    for i in range(0,len(vehicles)):
        clientes.append(vehicles[i][2])
    clientes.sort()
    clientes = list(dict.fromkeys(clientes))
    for i in range(0,len(clientes)):
        matriculas=[]
        for a in range(0,len(vehicles)):
            if(clientes[i]==vehicles[a][2]):
                matriculas.append(vehicles[a][0])
        print("NIF:",clientes[i],"Matrículas associadas:",matriculas)
