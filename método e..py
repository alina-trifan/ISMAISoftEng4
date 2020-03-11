import csv

from duraçao import Duracao

def inicio ():
    
    utilizador = []

    matricula = input("Introduza a matrícula: ").upper()
    
    duraçao = int(input("Indique a duração: "))

    while(validPlate(matricula) != True):
        print("Matrícula inválida, insira de novo: ")
        matricula = input("Introduza a matrícula: ").upper()
        
    utilizador.insert(0, matricula)
       
    while (validDuration(duracao)!= True):
        print ("Duração inválida, tente de novo!")
        duraçao = int(input("Indique a duração: "))
        
    utilizador.insert(o, duracao)
        
    print("Informações do utilizador: ", utilizador)
    

inicio()
