def evaluar_polinomio(coeficientes, x):
    return sum(coef * (x ** i) for i, coef in enumerate(reversed(coeficientes)))
def calcular_area_cain(coeficientes, n_rectangulos):
    base = 1 / n_rectangulos
    area_total = 0
    for i in range(n_rectangulos):
        x = i * base
        y = evaluar_polinomio(coeficientes, x)
        y = max(0, min(1, y))  # recorta al rango [0,1]
        area_total += y * base
    return area_total
def determinar_resultado(area_cain):
    area_abel = 1 - area_cain
    diferencia = abs(area_cain - area_abel)
    if diferencia <= 0.001:
        return "JUSTO"
    return "CAIN" if area_cain > area_abel else "ABEL"
def main():
    print("=== División de tierras entre Caín y Abel ===")
    print("Introduce los datos de cada función (grado, coeficientes y cantidad de rectángulos).")
    print("Cuando introduzcas un grado 20, el programa terminará.\n")
    while True:
        grado = int(input("Grado del polinomio (0 a 19, o 20 para salir): "))
        if grado == 20:
            print("Programa finalizado.")
            break
        print(f"Ingrese {grado + 1} coeficientes en orden de mayor a menor grado (separados por espacios):")
        coeficientes = list(map(float, input("Coeficientes: ").split()))
        while len(coeficientes) != grado + 1:
            print("Número incorrecto de coeficientes. Intenta de nuevo.")
            coeficientes = list(map(float, input("Coeficientes: ").split()))
        n = int(input("Número de rectángulos a usar para la suma de Riemann: "))
        area_c = calcular_area_cain(coeficientes, n)
        resultado = determinar_resultado(area_c)
        print(f"Resultado: {resultado}\n")
main()
