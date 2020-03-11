def pedirtempo():

    tempo= int(input('Qual o tempo que esteve estacionado no parque de estacionamento(Minutos)? '))

    
    while tempo<0:
        print ('Tem de ser um valor positivo')

        tempo= int(input('Qual o tempo que esteve estacionado no parque de estacionamento(Minutos)? '))

def pedirmatricula():

    matricula= str(input('Qual a sua Matrícula?'))

    '''validPlate (matricula)'''

    tempo = pedirtempo()


    thisdict = {
        matricula : tempo

    }

    print (thisdict)

    
    return (thisdict)


pedirmatricula()


    
