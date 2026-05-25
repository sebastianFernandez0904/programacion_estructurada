"""
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones:
1.- Con estructuras de control
2.- Sin funciones
"""

print("\033c")
numero=int(input("¿Que tabla desea multiplicar? "))
for num in range(1,11):
    multi=numero*num
    print(f"{numero} x {num}= {multi}")
    
"""
...
"""

print("\033c")
numero=int(input("¿Que tabla desea multiplicar? "))
num=1
while num<=10:
    multi=numero*num
    print(f"{numero} x {num}= {multi}")
    num+=1