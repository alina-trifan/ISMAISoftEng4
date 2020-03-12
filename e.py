from d import validarMatricula

DicionarioMatriculas = {}

def utilizacaoParque():
    while True:
        matriculaInserida = str(input("Introduza a matricula (sem separadores): "))
        matriculaInserida = matriculaInserida.upper()
        if validarMatricula(matriculaInserida):
            print("Matricula correta")
            DicionarioMatriculas["Matricula"] = matriculaInserida
            break;
        else:
            print("Matricula incorreta")

    duracao = 0
    while True:
        try:
            duracao = int(input("Introduza a duração (em minutos): "))
            if duracao <= 0:
                print("Inserir um número inteiro positivo")
                continue
            DicionarioMatriculas["Duração"] = duracao
            break
        except:
            print("Inserir um número inteiro positivo")
    return duracao

utilizacaoParque()
