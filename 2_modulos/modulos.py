#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    print("\033c")
    nombre=input("Escribr el nombre: ").strip() .upper()
    apellidos=input("Escribr los apellidos: ").strip() .upper()
    print(f"el nombre del alumno es: {nombre} {apellidos}")
#invocar la funcion
funcion1()
#3.- Funcion que recibe parametros y no regresa valor
def funcion3(nombre,apellidos):
    print("\033c")
    print(f"el nombre del alumno es: {nombre} {apellidos}")
#invocar la funcion
print("\033c")
nombre=input("Nombre: ").strip().upper()
apellidos=input("apellidos: ").strip().upper()
funcion3(nombre,apellidos)
#2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    print("\033c")
    nombre=input("Escribr el nombre: ").strip() .upper()
    apellidos=input("Escribr los apellidos: ").strip() .upper()
    return nombre,apellidos
#invocar la funcion
nombre,apellidos=funcion2()
print(nombre,apellidos)
#4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    print("\033c")
    nombre=nom
    apellidos=ape
    return nombre,apellidos
#invocar la funcion
nombre,apellidos=funcion4("Omar","Mancinas")
print(nombre,apellidos)
