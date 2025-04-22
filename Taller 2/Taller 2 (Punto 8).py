def entero_a_romano(num):
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    resultado = ""
    for valor, simbolo in valores:
        while num >= valor:
            resultado += simbolo
            num -= valor
    return resultado
def main():
    print("=== Convertidor de números enteros a romanos ===")
    print("Introduce números enteros positivos (0 para salir):\n")
    while True:
        try:
            numero = int(input("Número entero positivo: "))
            if numero == 0:
                print("Fin del programa.")
                break
            elif numero < 0:
                print("Por favor, ingresa solo números POSITIVOS.")
            else:
                romano = entero_a_romano(numero)
                print(f"{numero} en números romanos es: {romano}\n")
        except ValueError:
            print("Entrada no válida. Intenta con un número entero.\n")
main()
