import re

def correctMatricula(matricula):
    model8 = re.compile('^\d{2}[-][A-Z]{2}[-]\d{2}$')
    model6 = re.compile('^\d{2}[A-Z]{2}\d{2}$')
    matricula = matricula.upper();
    if len(matricula) == 6 and model6.match(matricula):
        correcao = list(matricula)
        matricula = (correcao[0]+correcao[1]+"-"+correcao[2]+correcao[3]+"-"+correcao[4]+correcao[5]);
        return matricula
    elif(len(matricula) == 8 and model8.match(matricula)):
        return matricula
    else:
        print("Matricula invalida.")
        return None
