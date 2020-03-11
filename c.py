def printClientPlates(c):
    clientes = []
    
    if not vehicles:
        print("Não existem clientes!")

    veiculos = len(vehicles)
     
    for x in range (veiculos):
        clientes.append(vehicles[x][2])

        
    clientes.sort()
    clientes = list(dict.fromkeys(clientes))
    
    
    for x in range(len(clientes)):
        
        matriculas = []
        
        for b in range(veiculos):
            
            if(clientes[x] == vehicles[b][2]):
                matriculas.append(vehicles[b][0])
                
                
        print("Contribuinte: ",clientes[x],"Matrículas: ",matriculas)
