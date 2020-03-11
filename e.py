import re
def inicio():
    duracao = ""
    i = 0 #contador para a duração
    p = 0 # contador para a matricula
    matricula = ""
    
    while p != 1:
        matricula = input("Introduza a matricula no formato 00-AA-00\n")
        if verifica_matricula(matricula) == None:
            print("Não introduziu uma matricula válida")
        else:
            print (matricula)
            p +=1
            
    while i != 1:        
        duracao = input("Introduza a duração\n")
        if duracao.isdigit() and int(duracao) > 0:
            print(duracao)
            i += 1
        else:
            print("Não introduziu um numero válido")        

def verifica_matricula (string):  
    match = re.search(r'\d{2}-[a-zA-Z]{2}-\d{2}', string)
    return None if match == None\
        else ()
# inicio do programa
inicio()
