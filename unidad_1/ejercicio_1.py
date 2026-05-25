#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    print("\033c")
    nombre=input("Escribr el nombre: ").strip() .upper()
    apellidos=input("Escribr los apellidos: ").strip() .upper()
    print(f"el nombre del alumno es: {nombre} {apellidos}")
#invocar la funcion
funcion1()