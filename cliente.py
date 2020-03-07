from veiculo import Veiculo
from operator import itemgetter

class Cliente:

    def __init__(self, l_nif, l_automoveis=[]):
        self.__nif = l_nif
        self.__automoveis = l_automoveis

    def adicionarVeiculo(self,l_matricula, l_marca):
        self.__automoveis.append(Veiculo(l_matricula, l_marca))
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

    def getNif(self):
        return str(self.__nif)

    def getVeiculoIndex(self, l_index):
        return self.__automoveis[l_index]

    def __repr__(self):
        return {'NIF':self.__nif}

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
