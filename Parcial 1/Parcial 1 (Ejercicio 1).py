"""
Escribir un programa que lea un número entero y determine si este es un
palíndromo, es decir, que se lee igual de izquierda a derecha que de derecha a
izquierda. Estos números se conocen como como capicúas.
12321, 454, 555, etc.
Nota: asumir que el número dado no tendrá ceros a la derecha.
"""
N=int(input("Escriba un numero entero: "))
B=N
#Se pide el numero al usuario y se guarda en otra variable
if N>=0:
    V=0
    while N>0:
        D=N%10
        V=D+V*10
        N//=10
        #Se voltea el numero para despues compararlo con la variable guardada
        #Si son iguales es capicua, de no serlo, no será capicua
    if V==B:
        print("Es capicua")
    else:
        print("No es capicua")
else:
    print("caracter invalido")