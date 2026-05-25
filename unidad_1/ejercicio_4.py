#4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    print("\033c")
    nombre=nom
    apellidos=ape
    return nombre,apellidos
#invocar la funcion
nombre,apellidos=funcion4("Omar","Mancinas")
print(nombre,apellidos)