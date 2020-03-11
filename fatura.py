class Fatura():

    idCount = 1

    def __init__(self, id, valor, cliente, ocupa):
        self.setId(id)
        self.setCliente(cliente)
        self.Valor(valor)
        self.setOcupa(ocupa)

    def getId(self):
        return self.__id

    def getValor(self):
        return self.__valor

    def getOcupa(self):
        return self.__ocupa

    def getCliente(self):
        return self.__cliente

    def setId(self,id):
        self.__id= idCount
        global idCount = idCount + 1

    def setValor(self,valor):
        if  isinstance(valor, number) == False or valor < 0:
            self.__valor= 0
        else:
            self.__valor= 0

    def setCliente(self,cliente):
        if  isinstance(cliente, Cliente) == False:
            self.__cliente = None
        else:
            self.__cliente = cliente

    def setOcupa(self,ocupa):
        if  isinstance(ocupa, Ocupa) == False:
            self.__ocupa = None
        else:
            self.__ocupa = ocupa

    def calcularValor(self, nif):
        if self.getCliente().getNif() = nif :
            
