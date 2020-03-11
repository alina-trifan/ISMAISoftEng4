import re
from a_b import vehicle

# função que imprime se a matrícula é válida 
def inicio():
    t = 0  # contador 
    matricula = ""
    
    while t != 1:
        matricula = input("Introduza a matrícula: \n")

        if validplates(matricula) == False:
            print("Matrícula fornecida [" + matricula + "] : Falso") # ou return falso
            t += 1
        else:
            print("Matrícula fornecida [" + matricula + "] : Verdadeiro")
            t += 1

# função que verifica se a matrícula é válida
def validplates (string):  
    match = re.search(r"[0-9]{2}[-][a-zA-Z]{2}[-][0-9]{2}", string)  
    return False if match == None\
        else ()

# início do programa
inicio()



