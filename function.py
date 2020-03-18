import re
from datetime import datetime
import pandas as pd
import csv

def correctMatricula(matricula): #metodo de correção de matricula
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

def registerSaida(matricula): #metodo para registar saida de veiculo do parque
    index = -1
    matricula = correctMatricula(str(matricula))
    vehicleExist = False
    with open('ocupacao.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter = ';')
        for row in reader:
            if (row[0] == str(matricula) and str(row[3]) == "None"):
                vehicleExist = True
                break
            index += 1
    if (vehicleExist == False):
        print("Mat: "+matricula)
        print("Veiculo não encontrado.")
    else:
        with open('ocupacao.csv') as csv_file:
            now = datetime.now()
            pandaReader = pd.read_csv(csv_file, sep = ';')
            pandaReader.iat[index, 3] = now.strftime("%Y-%m-%d %H:%M:%S.%f")
            pandaReader.iat[index, 4] = str(int(calcDurationMinutes(pandaReader.at[index, "2"], datetime.now())))
            pandaReader.iat[index, 5] = str(round(calcDurationMinutes(pandaReader.at[index, "2"], datetime.now()) * 0.01, 2))
            pandaReader.to_csv("ocupacao.csv", index=False, sep = ';')

def calcDurationMinutes(entrada, saida): #metodo para calucular duração de tempo em minutos
    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    diff = datetime.strptime(str(saida), datetimeFormat) - datetime.strptime(str(entrada), datetimeFormat)
    return diff.seconds / 60

def vehicleValidation(l_veiculo): #metodo para verificar se veiculo ja existe no arquivo ep1.csv
    with open('ep1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter = ';')
        for row in reader:
            if str(row[0]) == str(l_veiculo.getMatricula()):
                return True
        return False
