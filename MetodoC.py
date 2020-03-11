def c():
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

c()
