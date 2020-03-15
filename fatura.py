from datetime import datetime
import pandas as pd
import csv
from cliente import Cliente

class Fatura():

    idCount = 1

    def __init__(self, id, valorTotal = 0, cliente, ocupa = []):
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
        self.__id= idCount
        global idCount = idCount + 1

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

    def calcularValor(self, nif):
        valorTotal = 0
        l_ocupacoes = self.adicionarOcupa()
        for ocupa in l_ocupacoes:
            valorTotal += ocupa.getValor()
        self.setValorTotal(valorTotal)

    def adicionarOcupa(self):
        veiculos = []
        marcas = []
        ocupacoes = []
        dateNow =  datetime.now()
        with open('ep1.csv') as csv_file:
            readerEp = csv.reader(csv_file, delimiter = ';')
            for row in readerEp:
                if str(row[2]) == self.getCliente().getNif():
                    veiculos.append(Veiculo(str(row[0]), str(row[1])))

        with open('ocupacao.csv') as csv_file:
            readerOcup = csv.reader(csv_file, delimiter = ';')
            for row in readerOcup:
                for index in veiculos:
                    dateVerify = datetime.strptime(row[3], '%m/%d/%y %H:%M:%S')
                    if (str(row[0]) == veiculos[index].getMatricula() and dateVerify.month == dateNow.month and dateVerify.year == dateNow.year):
                        ocupacoes.append(Ocupa(veiculos[index]), datetime.strptime(row[2], '%m/%d/%y %H:%M:%S'), dateVerify, int(row[4]), float(row[5]))
        self.setOcupa(ocupacoes)
