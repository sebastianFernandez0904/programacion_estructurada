import random

def calcular_imc(peso, altura):
    """Calcula el IMC dado peso en kg y altura en metros."""
    return peso / (altura * altura)

def main():
    lista_imc = []
    
    while True:
        print("\n--- Calculadora de IMC ---")
        
        try:
            peso = float(input("Ingresa tu peso (kg): "))
            altura = float(input("Ingresa tu altura (m): "))
            
            if peso <= 0 or altura <= 0:
                print("Error: el peso y la altura deben ser mayores a 0.")
                continue
            
            imc = calcular_imc(peso, altura)
            lista_imc.append(imc)
            
            print(f"Tu IMC es: {imc:.2f}")
            
            if imc < 18.5:
                categoria = "Bajo peso"
            elif imc < 25:
                categoria = "Peso normal"
            elif imc < 30:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidad"
            
            print(f"Categoría: {categoria}")
        
        except ValueError:
            print("Error: ingresa un número válido.")
            continue
        
        continuar = input("\n¿Deseas calcular otro IMC? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    if lista_imc:
        # Convertir lista a set (conjunto) con valores únicos redondeados
        set_imc = set(round(x, 2) for x in lista_imc)
        
        # Calcular promedio
        promedio = sum(lista_imc) / len(lista_imc)
        
        # Orden aleatorio
        lista_aleatoria = lista_imc.copy()
        random.shuffle(lista_aleatoria)
        
        print("\n========== RESULTADOS FINALES ==========")
        print(f"Total de IMC calculados: {len(lista_imc)}")
        print(f"Promedio de IMC: {promedio:.2f}")
        print(f"IMC en orden aleatorio: {[round(x, 2) for x in lista_aleatoria]}")
        print(f"Conjunto (set) de IMC únicos: {set_imc}")
        print("========================================")

main()