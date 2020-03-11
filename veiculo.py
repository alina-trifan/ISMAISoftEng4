class Veiculo:

    def __init__(self, matricula, marca="indefinida"):
        self.__matricula = matricula
        self.__marca = marca

    def getMatricula(self):
        return self.__matricula

    def getMarca(self):
        return self.__marca

    def setMatricula(self, matricula):
        if  validPlate(matricula) == False:
            self.__matricula = None
        elif len(matricula) == 6 and validPlateVehicle(matricula):
            correcao = list(matricula)
            matricula = (correcao[0]+correcao[1]+"-"+correcao[2]+correcao[3]+"-"+correcao[4]+correcao[5]);
            self.__matricula = matricula
        else:
            self.__matricula = str(matricula)

    def setMarca(self, marca):
        if  isinstance(marca, str) == False:
            self.__marca= "indefinida"
        else:
            self.__marca = marca

    def validPlateVehicle(matricula):
        model8 = re.compile('^\d{2}[-][A-Z]{2}[-]\d{2}$')
        model6 = re.compile('^\d{2}[A-Z]{2}\d{2}$')
        matricula = matricula.upper();

        if len(matricula) == 8 and model8.match(m):
            return True

        elif len(matricula) == 6 and model6.match(m):
            return True
        else:
            return False

    def __repr__(self):
        return {'Matricula':self.getMatricula(), 'Marca':self.getMarca()}

    def __str__(self):
        return str(self.getMatricula())+'   '+str(self.getMarca())

    def copy(self):
        newcopy = self
        return newcopy
        __copy__ = copy

    def __eq__(self, other):
        if isinstance(other, Veiculo):
            return self.matricula == other.matricula
        return False
