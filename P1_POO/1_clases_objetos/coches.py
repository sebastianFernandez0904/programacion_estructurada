"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

#marca, color, modelo, velocidad, potencia y numero de acientos y con las operacionesn de acelerar. que los atributos de la clase sean privados y que se pueda acceder a ellos mediante metodos sean publicos    

class Coches:
    marca= ""
    color="sin color"
    velocidad = 0
    potencia = 0
    asientos = 0

    def acelerar(self):
        #pass
        self.velocidad+=1

    def frenar(self):
        #pass
        self.velocidad-=1

coche1= Coches() #objeto= una estructura de datos
coche2= Coches() #son identicos examen. Dos tablas de clase de objetos.


print(f" el color del coche uno es= {coche1.color}")

coche1.color= "verde y azul"
print(f" el color del coche uno es= {coche1.color}")

coche2.color= "verde y rosa"

print(f" el color del coche dos es= {coche2.color}")

print(f"la velocidad inicial del coche es: {coche1.velocidad}")

for i in range(1, 11):
    coche1.acelerar()

print(f"la velocidad final del coche es: {coche1.velocidad}")

# _marca= cuando hay una herencia ya no se puede utilizar afuera
#  los atributos no deben ser accedidos directamenta, no es una buena practica que se cambien los atributos directamente, se va a hacer mas adelante con get y set, por eso tambien es importante que sean privados o protegidos, jamas publicos para evitar