"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class Coches:
    def __init__(self, color, marca, velocidad):
        self.__color = color
        self.__marca = marca
        self.__velocidad = velocidad

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def tocar_claxon(self):
        print("pi pi pi")

coche1 = Coches("Rojo", "Toyota", 120)
coche2= Coches("Azul", "Nissan", 180)

print(f"El claxon del coche1 hace: ")
coche2.tocar_claxon()

coche1.acelerar

#Instanciar o crear objetos de la clase Coches






