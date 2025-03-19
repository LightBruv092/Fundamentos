"""
Escribir un programa que lea un número entero y determine cuales de sus
cifras son pares y cuales son impares. Además, el programa debe contar cuantas
cifras tiene el número en total.
"""
N=str(input("Ingrese un numero entero:"))
#se pide un numero y se guarda como cadena para luego contar cuantas cifras tiene
D=len(N)
print("El número tiene",D,"cifras" )
for x in range(1,D+1):
    F=int(N[x-1])
    #se transforma a enteros cifra a cifra pa evaluar sus residuos con 2
    #si el residuo con 2 de la cifra es 0 será par, sino será impar
    if F%2==0:
        print("El numero",F,"es par.")
    else:
        print("El numero", F, "es impar.")



