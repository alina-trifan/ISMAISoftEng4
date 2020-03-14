import csv
from veiculo import *
from datetime import datetime
import pandas as pd
from function import *

def registerSaida(matricula):
    index = 0
    vehiclePark = False
    with open('ocupacao.csv') as csv_file:
        pandaReader = pd.read_csv(csv_file, sep = ';')
        for row in pandaReader:
            if (pandaReader.at[index, "3"] == "None" and pandaReader.at[index, "0"] == correctMatricula(matricula)):
                pandaReader.iat[index, 3] = str(datetime.now())
                pandaReader.iat[index, 4] = str(int(calcDurationMinutes(pandaReader.at[index, "2"], datetime.now())))
                pandaReader.iat[index, 5] = str(int(calcDurationMinutes(pandaReader.at[index, "2"], datetime.now())) * 0.1)
                vehiclePark = True
                break
            index += 1
        pandaReader.to_csv("ocupacao.csv", index=False, sep = ';')
    if (vehiclePark == False):
        return "Veiculo não encontrado."

def calcDurationMinutes(entrada, saida):
    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    diff = datetime.strptime(str(saida), datetimeFormat) - datetime.strptime(str(entrada), datetimeFormat)
    return diff.seconds / 60

class Ocupa:

    def __init__(self, veiculo, entrada = datetime.now(), saida= None):
        validate = True
        with open('ocupacao.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter = ';')
            for row in reader:
                if str(row[3]) == "None" and str(row[0]) == veiculo.getMatricula():
                    print("Veiculo já se encontra dentro do estacionamento.")
                    validate = False
                    break
        if (validate == False):
            pass
        else:
            if veiculo.getMatricula() ==None:
                pass
            elif self.vehicleValidation(veiculo) == False and veiculo.getMatricula():
                print("Veiculo não registado.")
                nif = input("Adicionar NIF : ")
                with open('ep1.csv', 'a+', newline='') as csv_file:
                    ep1_writer = csv.writer(csv_file, delimiter=';')
                    ep1_writer.writerow([veiculo.getMatricula(), veiculo.getMarca(), nif])
                self.setVeiculo(veiculo)
                self.setEntrada(entrada)
                self.setSaida(saida)
                with open('ocupacao.csv', 'a+', newline='') as csv_file:
                    ocupa_writer = csv.writer(csv_file, delimiter=';')
                    ocupa_writer.writerow([veiculo.getMatricula(), veiculo.getMarca(), str(entrada), str(saida), "DurationNull", "ValueNull"])
            else:
                self.setVeiculo(veiculo)
                self.setEntrada(entrada)
                self.setSaida(saida)
                with open('ocupacao.csv', 'a+', newline='') as csv_file:
                    ocupa_writer = csv.writer(csv_file, delimiter=';')
                    ocupa_writer.writerow([veiculo.getMatricula(), veiculo.getMarca(), str(entrada), str(saida), "DurationNull", "ValueNull"])


    def getVeiculo(self):
        return self.__veiculo

    def getEntrada(self):
        return self.__entrada

    def getSaida(self):
        return self.__saida

    def getDuracao(self):
        return self.__duracao

    def setVeiculo(self,l_veiculo):
        if  isinstance(l_veiculo, Veiculo) == False or self.vehicleValidation(l_veiculo) == False:
            pass
        else:
            self.__veiculo = l_veiculo

    def setEntrada(self,l_entrada):
        if  isinstance(l_entrada, datetime) == False or l_entrada > datetime.now():
            self.__entrada=datetime.now()
        else:
            self.__entrada=l_entrada

    def setSaida(self,l_saida):
        if  isinstance(l_saida, datetime) == False or l_saida > datetime.now():
            self.__saida= None
        else:
            self.__saida=l_saida

    def vehicleValidation(self, l_veiculo):
        with open('ep1.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter = ';')
            for row in reader:
                if str(row[0]) == str(l_veiculo.getMatricula()):
                    return True
            return False

    def __repr__(self):
        return {'Veiculo':self.getVeiculo(), 'Entrada': self.getEntrada().strftime("%m/%d/%Y, %H:%M:%S")}

    def __str__(self):
        return str(self.getVeiculo())+' Entrada = '+self.getEntrada().strftime("%m/%d/%Y, %H:%M:%S")

    def __eq__(self, other):
        if isinstance(other, Ocupa):
            if(self.getEntrada() == other.getEntrada() and self.getVeiculo() == other.getVeiculo()):
                return True
        return False
