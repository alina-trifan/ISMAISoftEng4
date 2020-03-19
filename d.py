import re
from a_b import vehicle

# função que permite verificar se a matrícula é válida
def inicio():
    t = 0  # contador 
    matricula = ""
    
    while t != 1:
        matricula = input("Introduza a matrícula no formato 00-XX-00: \n")

        if verifica_matricula(matricula) == False:
            print("Matrícula fornecida [" + matricula + "] : Invalida") # ou return falso
        
        else:
            print("Matrícula fornecida [" + matricula + "] : Verdadeiro")
            t += 1

def verifica_matricula (string):  
    match = bool(re.search(r'\d{2}-[a-zA-Z]{2}-\d{2}', string))
    return match

# início do programa
inicio()


