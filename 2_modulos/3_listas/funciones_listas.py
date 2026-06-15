print("\033c")
paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil"]
numeros=[23,45,8,24]
varios=[33,3.1416,"Hola",True]
vacio=[]

print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[0]+" "+paises[3])
for i in paises:
    print(i)

for i in range(0,5):
    print(paises[i])

paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil"]
print(paises)
paises.sort()
print(paises)
paises.reverse()
print(paises)

paises.append("Honduras")
print(paises)

paises.insert(1,"Argentina")
print(paises)
paises.insert(100,"Panama")
print(paises)
paises.append(23)
paises.append(3)
print(paises)
paises.sort()
print(paises)

#1er forma
paises.pop(4)
print(paises)

#2da forma
paises.remove("EUA")
print(paises)

#buscar
buscar="Brasil" in paises
if buscar==True:
    print("Soy True")
else:
    print("Soy False")

#contar numeros de veces que aprece un elemento dentro de una lista
numeros=[23,45,24,8,23,50,23]
num=int(input("Dame el numero a contar: "))
cuantas=numeros.count(num)
print(f"El numero {num}aparece: {cuantas} veces")

#conocer la posicion o nindice en el que  se encuentra un elemento de la lisat
posicion=numeros.index(50)
print(f"Estoy en la posicion: {posicion}")

#recorrer lista
for i in paises:
    print (i)

#2do forma 
for i in range(0,len(paises)):
    print(paises[i])

#unir el contenido de una lita  dentro de otera lista
numeros1=[23,45,24,8,23,50,23]
print(numeros1)
numeros2= [100,-100]
print(numeros2)
numeros1.extend(numeros2)
print(numeros1)

#crear a partit de las listas de numeros q y 2 un¿n resultsnte y mostrat el contenido
numeros1.short()
numeros1.reverse()
print(numeros1)

#ejemplo 1
numeros=[23,45,23,33,25,100,-100]
print(numeros)

lista="["
i=0
while i<len(numeros):
    lista+=f"{numeros[i]}"
    i+=1
print(f"{lista}]")

#ejemplo 2 
palabras=["hola","NBA","ganador","perdedor" ]
palabra=input("Dame la palabra a buscas:")

#1er forma
if palabra in palabras:
    print(f"La palabra {palabra} si esta en la lista")
else:    print(f"La palabra {palabra} no esta en la lista")

#2da forma
palabras=["hola","NBA","ganador","perdedor" ]
palabra=input("Dame la palabra a buscas:")

lista[]
true="S"
while true:
    lista:append(("Dame un valor a la lista".upper().strip()))






agenda=[
        ["carlos","618234567"]
        ["juan","6182334567"]
        ["Tony"]

    
]
    