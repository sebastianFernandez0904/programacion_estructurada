#2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    print("\033c")
    nombre=input("Escribr el nombre: ").strip() .upper()
    apellidos=input("Escribr los apellidos: ").strip() .upper()
    return nombre,apellidos
#invocar la funcion
nombre,apellidos=funcion2()
print(nombre,apellidos)