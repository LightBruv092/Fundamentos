"""
Construir un programa que permita escoger entre dos operaciones, usando un
menú. La primera, leer un número n y determinar si es par o impar. La segunda,
leer un número n y determinar si es primo o no. n debe ser un número entero
positivo. El programa debe detectar si la opción escogida es o no válida.
"""
N=int(input("Ingrese un numero entero positivo: "))
if N>=0:
    #Se imprime un menu para que el usuario elija
    print("Menu")
    print("Elija una opción:")
    print("Opcion 1: Determinar si es par o impar")
    print("Opcion 2: Determinar si es primo o no")
    O=int(input())
    #Solo se procesará cuando la opcion digitada sea 1 o 2
    if O==1 or O==2:
        print("Opcion valida.")
        if O==1:
            #se saca el residuo del numero con 2, si es 0 es par, sino es impar
            if N%2==0:
                print("Es par.")
            else:
                print("Es impar.")
        else:
            #Se cuentan los divisores del numero, si son 2 son primos, sino no lo son
            C=0
            for x in range(1, N+1):
                if N%x==0:
                    C+=1
            if C==2:
                print("Es primo.")
            else:
                print("No es primo.")
    else:
        print("Opcion invalida.")
else:
    print("Numero fuera del rango.")