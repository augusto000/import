
from game.vehiculos import Vehiculos


class Moto(Vehiculos):
    def __init__(self) :
        self.__patente=""

    def setPatente(self, patente):
        self.__patente=patente
    def getPatente(self):
        return "{}".format(self.__patente)

ObjMoto = Moto()
ObjMoto.setMarca(input("Ingrese la Marca de la Moto : "))
ObjMoto.setModelo(input("Ingrese el Modelo de la Moto :"))
print(ObjMoto.getMarca())

print(ObjMoto.getModelo())

            

