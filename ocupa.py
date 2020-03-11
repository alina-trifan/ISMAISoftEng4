import csv
from veiculo import Veiculo
from datetime import datetime

class Ocupa:

    def __init__(self, veiculo, entrada = datetime.now(), saida= datetime.now()):
        self.setVeiculo(veiculo)
        self.setEntrada(entrada)
        self.setSaida(saida)
        with open('ocupacao.csv', mode='w') as csv_file:
            ocupa_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ocupa_writer.writerow([veiculo.getMatricula(), str(entrada), str(saida)])

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
            self.__veiculo = None
        else:
            self.__veiculo = l_veiculo

    def setEntrada(self,l_entrada):
        if  isinstance(l_entrada, datetime) == False or l_entrada > datetime.now():
            self.__entrada=datetime.now()
        else:
            self.__entrada=l_entrada

    def setSaida(self,l_saida):
        if  isinstance(l_saida, datetime) == False or l_saida > datetime.now():
            self.__saida=datetime.now()
        else:
            self.__saida=l_saida

    def vehicleValidation(self, l_veiculo):
        with open('ep1.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter = ';')
            for row in reader:
                if str(row[0]) == str(l_veiculo.getMatricula()):
                    return True
            return False

    def calcDurationMinutes(self):
        difference = self.getEntrada - self.getSaida
        difference_out = difference.seconds / 60
        return difference_out

    def __repr__(self):
        return {'Veiculo':self.getVeiculo(), 'Entrada': str(self.getEntrada()), 'Saida': str(self.getSaida())}

    def __str__(self):
        return 'Veiculo = '+self.getVeiculo()+' Entrada = '+str(self.getEntrada())+'Saida = '+str(self.getSaida())

    def __eq__(self, other):
        if isinstance(other, Ocupa):
            if(self.getEntrada() == other.getEntrada() and self.getVeiculo() == other.getVeiculo()):
                return True
        return False

o1 = Ocupa(Veiculo("66-SS-66", "Tesla"))
