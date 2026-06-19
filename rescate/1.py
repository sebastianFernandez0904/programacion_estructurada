def calcular_area(base, altura):
    return (base * altura) / 2

def main():
    areas = []

    while True:
        print("\n--- Cálculo de Área de Triángulo Rectángulo ---")
        
        try:
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
        except ValueError:
            print("Por favor ingresa valores numéricos válidos.")
            continue

        area = calcular_area(base, altura)
        areas.append(area)
        print(f"El área del triángulo es: {area:.2f}")

        continuar = input("\n¿Deseas calcular otra área? (s/n): ").strip().lower()
        if continuar != 's':
            break

    if areas:
        areas_tupla = tuple(sorted(areas, reverse=True))
        promedio = sum(areas) / len(areas)

        print("\n========== RESULTADOS FINALES ==========")
        print(f"Promedio de todas las áreas: {promedio:.2f}")
        print(f"Áreas en orden descendente (tupla): {areas_tupla}")
        print("========================================")

main()