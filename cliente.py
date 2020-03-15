from veiculo import Veiculo
from operator import itemgetter
import csv

class Cliente:

    def __init__(self, nif):
        self.setNif(nif)
        automoveis = []
        with open('ep1.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter = ';')
            for row in reader:
                if(row[2] == nif):
                    automoveis.append(Veiculo(str(row[0]),str(row[1])))
            self.setAutomoveis(automoveis)

    def getNif(self):
        return str(self.__nif)

    def getAutomoveis(self):
        return self.__automoveis

    def setNif(self,nif):
        if  int(nif) < 0:
            self.__nif = "Nope"
        elif len(str(nif)) < 9 or str(nif).isnumeric() == False:
            self.__nif = None
        else:
            self.__nif = nif

    def setAutomoveis(self,automoveis):
        if  isinstance(automoveis, list) or all(isinstance(x, Veiculo) for x in automoveis) == False:
            self.__automoveis = []
        else:
            self.__automoveis = automoveis


    def adicionarVeiculo(self,matricula, marca):
        self.__automoveis.append(Veiculo(matricula, marca))
        self.ordenarVeiculos()

    def removerVeiculo(self, l_veiculo):
        self.__automoveis.remove(l_veiculo)

    def removerTodosVeiculo(self):
        self.__automoveis = []

    def verificarVeiculo(self, l_veiculo):
        for i in range(self.numeroVeiculos()):
            if self.__automoveis[i].getMatricula() == l_veiculo.getMatricula():
                return True
            else:
                break
        return False

    def ordenarVeiculos(self):
        self.__automoveis = sorted(self.__automoveis, key=lambda veiculo: veiculo.getMatricula()).copy()

    def numeroVeiculos(self):
        return len(self.__automoveis)


    def getVeiculoIndex(self, l_index):
        return self.__automoveis[l_index]

    def __repr__(self):
        return {'NIF':self.getNif()}

    def __str__(self):
        return 'NIF = '+self.getNif()

    def copy(self):
        newcopy = self
        return newcopy
        __copy__ = copy

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.__nif == other.__nif
        return False
