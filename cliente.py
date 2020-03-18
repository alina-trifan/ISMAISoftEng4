from veiculo import Veiculo
from operator import itemgetter
import csv

class Cliente: #classe referente ao cliente

    def __init__(self, nif): #construtor
        self.setNif(nif)
        automoveis = []
        with open('ep1.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter = ';')
            for row in reader:
                if(row[2] == nif):
                    automoveis.append(Veiculo(str(row[0]),str(row[1])))
            self.setAutomoveis(automoveis)

    def getNif(self): #encapsulamento
        return str(self.__nif)

    def getAutomoveis(self): #encapsulamento
        return self.__automoveis

    def setNif(self,nif): #encapsulamento
        if  int(nif) < 0:
            self.__nif = "Nope"
        elif len(str(nif)) < 9 or str(nif).isnumeric() == False:
            self.__nif = None
        else:
            self.__nif = nif

    def setAutomoveis(self,automoveis): #encapsulamento
        if  isinstance(automoveis, list) or all(isinstance(x, Veiculo) for x in automoveis) == False:
            self.__automoveis = []
        else:
            self.__automoveis = automoveis


    def adicionarVeiculo(self,matricula, marca): #função para adicionar um objeto do tipo veiculo ao atributo de lista do cliente
        v1 = Veiculo(matricula, marca)
        if self.verificarVeiculo(v1):
            self.__automoveis.append(Veiculo(matricula, marca))
            self.ordenarVeiculos()
        else:
            pass

    def removerVeiculo(self, l_veiculo): #função para remvover um objeto do tipo veiculo ao atributo de lista do cliente
        self.__automoveis.remove(l_veiculo)

    def removerTodosVeiculo(self): #função para limpar o atributo de lista de um cliente
        self.__automoveis = []

    def verificarVeiculo(self, l_veiculo):  #verificar se veiculo ja existe no atributo lista
        for i in range(self.numeroVeiculos()):
            if self.__automoveis[i].getMatricula() == l_veiculo.getMatricula():
                return True
            else:
                break
        return False

    def ordenarVeiculos(self): #função para ordenar veiculos de forma crescente
        self.__automoveis = sorted(self.__automoveis, key=lambda veiculo: veiculo.getMatricula()).copy()

    def numeroVeiculos(self): #função para retonar tamanho da lista de automoveis
        return len(self.__automoveis)

    def __repr__(self): #função de representação de um objeto, caso o tostring não resulte
        return {'NIF':self.getNif()}

    def __str__(self): #função to String, imprimi o objeto em forma de string
        return 'NIF = '+self.getNif()

    def copy(self): #função para copiar um cliente
        newcopy = self
        return newcopy
        __copy__ = copy

    def __eq__(self, other): #função para determinar se instancias de objetos são iguais
        if isinstance(other, Cliente):
            return self.__nif == other.__nif
        return False
