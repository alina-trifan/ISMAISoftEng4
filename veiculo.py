class Veiculo:

    def __init__(self, l_matricula, l_marca="indefinida"):
        self.__matricula = str(l_matricula)
        self.__marca = l_marca

    def getMatricula(self):
        return str(self.__matricula)

    def __repr__(self):
        return {'Matricula':self.__matricula, 'Marca':self.__marca}

    def __str__(self):
        return 'Matricula = '+self.__matricula+', Marca = '+str(self.__marca)

    def copy(self):
        newcopy = self
        return newcopy
        __copy__ = copy

    def __eq__(self, other):
        if isinstance(other, Veiculo):
            return self.__matricula == other.__matricula
        return False
