import re

class Veiculo: #classe que representa a abstração de veiculo

    def __init__(self, matricula, marca="indefinida"): #construtor
        self.setMatricula(matricula)
        self.__marca = marca

    def getMatricula(self): #encapsulamento
        return self.__matricula

    def getMarca(self): #encapsulamento
        return self.__marca

    def setMatricula(self, matricula): #encapsulamento
        model8 = re.compile('^\d{2}[-][A-Z]{2}[-]\d{2}$')
        model6 = re.compile('^\d{2}[A-Z]{2}\d{2}$')
        matricula = matricula.upper();
        if len(matricula) == 6 and model6.match(matricula):
            correcao = list(matricula)
            matricula = (correcao[0]+correcao[1]+"-"+correcao[2]+correcao[3]+"-"+correcao[4]+correcao[5]);
            self.__matricula = matricula
        elif(len(matricula) == 8 and model8.match(matricula)):
            self.__matricula = matricula
        else:
            print("Matricula invalida.")
            self.__matricula = None

    def setMarca(self, marca): #encapsulamento
        if  isinstance(marca, str) == False:
            self.__marca= "indefinida"
        else:
            self.__marca = marca

        if len(matricula) == 8 and model8.match(m):
            return True

        elif len(matricula) == 6 and model6.match(m):
            return True
        else:
            return False

    def __repr__(self): #função de representação de um objeto, caso o tostring não resulte
        return {'Matricula':self.getMatricula(), 'Marca':self.getMarca()}

    def __str__(self): #função to String, imprimi o objeto em forma de string
        return str(self.getMatricula())+'   '+str(self.getMarca())

    def copy(self): #função para copiar um objeto desta classe
        newcopy = self
        return newcopy
        __copy__ = copy

    def __eq__(self, other): #função para determinar se instancias de objetos são iguais
        if isinstance(other, Veiculo):
            return self.getMatricula() == other.getMatricula()
        return False
