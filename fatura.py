from datetime import datetime
import pandas as pd
import csv
from cliente import Cliente
from veiculo import Veiculo

class Fatura():

    idCount = 1

    def __init__(self, cliente, valorTotal = 0, ocupa = []):
        self.setId(id)
        self.setCliente(cliente)

    def getId(self):
        return self.__id

    def getValorTotal(self):
        return self.__valorTotal

    def getOcupa(self):
        return self.__ocupa

    def getCliente(self):
        return self.__cliente

    def setId(self,id):
        self.__id= Fatura.idCount
        Fatura.idCount += 1

    def setValorTotal(self,valorTotal):
        if  isinstance(valorTotal, number) == False or valorTotal < 0:
            self.__valorTotal= 0
        else:
            self.__valorTotal= valorTotal

    def setCliente(self,cliente):
        if  isinstance(cliente, Cliente) == False:
            self.__cliente = None
        else:
            self.__cliente = cliente

    def setOcupa(self,ocupa):
        self.__ocupa = ocupa

    def calcularValor(self):
        valorTotal = 0
        l_ocupacoes = self.adicionarOcupa()
        for ocupa in l_ocupacoes:
            valorTotal += ocupa.getValor()
        self.setValorTotal(valorTotal)

    def adicionarOcupa(self):
        veiculosVerify = []
        ocupacoes = []
        dateNow =  datetime.now()
        cont = 0

        with open('ep1.csv') as csv_file:
            readerEp = csv.reader(csv_file, delimiter = ';')
            for row in readerEp:
                if str(row[2]) == self.getCliente().getNif():
                    veiculo = Veiculo(str(row[0]), str(row[1]))
                    print(veiculo)
                    veiculosVerify.append(veiculo)
                    print(veiculosVerify)

        with open('ocupacao.csv') as csv_file:
            readerOcup = csv.reader(csv_file, delimiter = ';')
            for index in readerOcup:
                for i in range(len(veiculosVerify)):
                    if cont > 0:
                        dateVerify = datetime.strptime(index[3], '%m/%d/%y %H:%M:%S')
                        if (str(index[0]) == veiculosVerify[i].getMatricula() and dateVerify.month == dateNow.month and dateVerify.year == dateNow.year and index[3] != "None"):
                            ocupacoes.append(Ocupa(veiculosVerify[i]), datetime.strptime(index[2], '%m/%d/%y %H:%M:%S'), dateVerify, int(index[4]), float(index[5]))
                    ++cont
        print(ocupacoes)
        self.setOcupa(ocupacoes)
