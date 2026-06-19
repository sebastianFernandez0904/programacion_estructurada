import math

def calcular_area(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio * radio

def main():
    areas = []
    
    while True:
        try:
            radio = float(input("Ingresa el radio del círculo: "))
            if radio < 0:
                print("El radio no puede ser negativo. Intenta de nuevo.")
                continue
            
            area = calcular_area(radio)
            areas.append(area)
            print(f"Área del círculo con radio {radio}: {area:.4f}")
        
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue
        
        continuar = input("¿Deseas calcular otra área? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    if areas:
        
        promedio = sum(areas) / len(areas)
        
        
        tupla_descendente = tuple(sorted(areas, reverse=True))
        
        print("\n===== RESULTADOS FINALES =====")
        print(f"Promedio de todas las áreas: {promedio:.4f}")
        print(f"Tupla con áreas en orden descendente: {tupla_descendente}")
    else:
        print("No se calculó ninguna área.")

main()