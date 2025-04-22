def encontrar_pares(lista, objetivo):
    vistos = set()
    pares_unicos = set()
    for numero in lista:
        complemento = objetivo - numero
        if complemento in vistos:
            par = tuple(sorted((numero, complemento)))
            pares_unicos.add(par)
        vistos.add(numero)
    if pares_unicos:
        print("\nPares que suman", objetivo, ":")
        for a, b in sorted(pares_unicos):
            print(f"{a}, {b}")
    else:
        print("\nNo se encontraron pares que sumen", objetivo)
def main():
    print("=== Encontrar pares que suman un valor objetivo ===")
    entrada = input("Ingresa una lista de enteros separados por comas (ej. 1,2,3,4,5): ")
    lista = list(map(int, entrada.split(',')))
    objetivo = int(input("Ingresa la suma objetivo: "))
    encontrar_pares(lista, objetivo)
main()