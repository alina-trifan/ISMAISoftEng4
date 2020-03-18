from datetime import datetime
import pandas as pd
import csv
from cliente import Cliente
from veiculo import Veiculo
from ocupa import Ocupa

class Fatura():

    def __init__(self, cliente, valorTotal = 0, ocupa = []): #construtor
        self.setCliente(cliente)

    def getValorTotal(self): #encapsulamento
        return self.__valorTotal

    def getOcupa(self): #encapsulamento
        return self.__ocupa

    def getCliente(self): #encapsulamento
        return self.__cliente

    def setValorTotal(self,valorTotal): #encapsulamento
        if  isinstance(valorTotal, float) == False or valorTotal < 0:
            self.__valorTotal= 0
        else:
            self.__valorTotal= valorTotal

    def setCliente(self,cliente): #encapsulamento
        if  isinstance(cliente, Cliente) == False:
            self.__cliente = None
        else:
            self.__cliente = cliente

    def setOcupa(self,ocupa): #encapsulamento
        self.__ocupa = ocupa

    def calcularValor(self): #função para calcular valor total da fatura
        valorTotal = 0
        l_ocupacoes = self.adicionarOcupa().copy()
        for ocupa in l_ocupacoes:
            valorTotal += ocupa.getValor()
        self.setValorTotal(valorTotal)

    def adicionarOcupa(self): #adicionar uma ocupaçao do parque ao atributo de lista do respectivo objecto a fatura
        ocupacoes = []
        dateNow =  datetime.now()

        with open('ep1.csv') as csv_file:
            readerEp = csv.reader(csv_file, delimiter = ';')
            for i in readerEp:
                if str(i[2]) == self.getCliente().getNif():
                    veiculo = Veiculo(str(i[0]), str(i[1]))
                    #print(veiculo)
                    with open('ocupacao.csv') as csv_file:
                        readerOcup = csv.reader(csv_file, delimiter = ';')
                        cont=0
                        for row in readerOcup:
                            #print(row[0])
                            if (str(row[0]) == veiculo.getMatricula() and row[3] != "None"):
                                dateVerify = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
                                if (dateVerify.month == dateNow.month and dateVerify.year == dateNow.year): #verificação do mes, a impressão das faturas seria mensal
                                    ocupaFinder = Ocupa(veiculo, datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S.%f"), dateVerify, int(row[4]), float(row[5]))
                                    #print(ocupaFinder)
                                    ocupacoes.insert(cont, ocupaFinder)
                            ++cont
        self.setOcupa(ocupacoes)
        return ocupacoes

    def copy(self): #função para copiar um cliente
        newcopy = self
        return newcopy
        __copy__ = copy
