def es_triangular_superior(matriz):
    n = len(matriz)
    for i in range(1, n):
        for j in range(i):
            if matriz[i][j] != 0:
                return False
    return True
def main():
    print("=== Verificación de matrices triangulares superiores ===")
    print("Ingresa una matriz cuadrada por bloques.")
    print("Primero escribe el número de filas y columnas (ej. 3 3).")
    print("Luego, escribe cada fila de la matriz separada por espacios.")
    print("Para terminar, escribe '0 0'.\n")
    while True:
        try:
            dims = input("Número de filas y columnas (ej. 3 3 o 0 0 para salir): ")
            f, c = map(int, dims.split())
            if f == 0 and c == 0:
                print("Fin del programa.")
                break
            if f != c:
                print("La matriz no es cuadrada. Resultado: NO\n")
                for _ in range(f):
                    input("Fila (omitida): ")
                continue
            matriz = []
            for i in range(f):
                fila = list(map(int, input(f"Fila {i+1}: ").split()))
                while len(fila) != c:
                    print("Cantidad incorrecta de elementos. Intenta de nuevo.")
                    fila = list(map(int, input(f"Fila {i+1}: ").split()))
                matriz.append(fila)
            resultado = "SI" if es_triangular_superior(matriz) else "NO"
            print(f"Resultado: {resultado}\n")
        except ValueError:
            print("Entrada no válida. Intenta de nuevo.\n")
main()