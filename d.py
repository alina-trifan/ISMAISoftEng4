import re

def validarMatricula(matriculaInserida):
    formato_matricula = re.compile('[0-9]{2}[A-Z]{2}[0-9]{2}$')
    if formato_matricula.match(matriculaInserida):
        matricula = True
    else:
        matricula = False
    return matricula
