#3.- Funcion que recibe parametros y no regresa valor
def funcion3(nombre,apellidos):
    print("\033c")
    print(f"el nombre del alumno es: {nombre} {apellidos}")
#invocar la funcion
print("\033c")
nombre=input("Nombre: ").strip().upper()
apellidos=input("apellidos: ").strip().upper()
funcion3(nombre,apellidos)