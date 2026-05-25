"""
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones:
1.- Con estructuras de control
2.- Con funciones
"""

# Limpia la pantalla de la consola
print("\033c")

# Definición de la función que calcula e imprime una sola fila de la tabla
def calcular_e_imprimir_linea(num_tabla, multiplicador):
    multi = num_tabla * multiplicador
    print(f"{num_tabla} x {multiplicador} = {multi}")

# Solicitar los datos al usuario
num_tabla = int(input("¿Qué tabla desea multiplicar? "))

# Estructura de control (for) que va del 1 al 10
for i in range(1, 11):
    calcular_e_imprimir_linea(num_tabla, i)
    