def addParkEntry():
   
    
    
    matx = input('Introduz a matricula: ')
    
    while (validPlate(matx) !=True):
            print("Invalida!")
            matx = input('Introduz a matricula novamente: ')

    matriculas.append(matx)
    
        
        
        
    durx=int(input('Duração: '))
    if durx<0:
        print('Invalida!')
            
    else:
        duracao.append(durx)
        print(matriculas)
        print(duracao)
        

    return matriculas
    return duracao
