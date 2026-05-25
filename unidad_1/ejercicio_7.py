"""
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones:
1.- Sin estructuras de control
2.- Con funciones
"""

print("\033c")
def tabla(num_tabla,num):
    multi=num_tabla*num
    print(f"{num_tabla} x {num}= {multi}")
    num+=1
    return num

num_tabla=int(input("¿que tabla desea multiplicar? "))
num=1

num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)