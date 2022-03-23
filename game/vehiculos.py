class Vehiculos():
    def __init__(self):
        self.__modelo=""
        self.__marca=""
        print("Vehiculos..")
        

    def setMarca(self, marca):
        self.__marca=marca
    def getMarca(self):
        return "{}".format(self.__marca)        
    
    def setModelo(self, modelo):
        self.__modelo=modelo
    def getModelo(self):
        return "{}".format(self.__modelo)

