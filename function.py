import re
from datetime import datetime
import pandas as pd
import csv

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

def registerSaida(matricula):
    index = 0
    vehiclePark = False
    matricula = correctMatricula(matricula)
    with open('ocupacao.csv') as csv_file:
        pandaReader = pd.read_csv(csv_file, sep = ';')
        for row in pandaReader:
            if (pandaReader.at[index, "3"] == "None" and pandaReader.at[index, "0"] == matricula):
                pandaReader.iat[index, 3] = str(datetime.now())
                pandaReader.iat[index, 4] = str(int(calcDurationMinutes(pandaReader.at[index, "2"], datetime.now())))
                pandaReader.iat[index, 5] = str(round(calcDurationMinutes(pandaReader.at[index, "2"], datetime.now()) * 0.1, 2))
                vehiclePark = True
                break
            index += 1
        pandaReader.to_csv("ocupacao.csv", index=False, sep = ';')
    if (vehiclePark == False):
        print("Veiculo não encontrado.")

def calcDurationMinutes(entrada, saida):
    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    diff = datetime.strptime(str(saida), datetimeFormat) - datetime.strptime(str(entrada), datetimeFormat)
    return diff.seconds / 60

def vehicleValidation(l_veiculo):
    with open('ep1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter = ';')
        for row in reader:
            if str(row[0]) == str(l_veiculo.getMatricula()):
                return True
        return False
