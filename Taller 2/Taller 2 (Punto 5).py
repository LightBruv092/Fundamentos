import math
import random
import matplotlib.pyplot as plt
def vector_unitario_aleatorio():
    ang = random.uniform(0, 2 * math.pi)
    return [math.cos(ang), math.sin(ang)]
def leer_vector():
    x = float(input("Componente x: "))
    y = float(input("Componente y: "))
    return [x, y]
def proyectar(v, u):
    escalar = v[0]*u[0] + v[1]*u[1]
    return [escalar * u[0], escalar * u[1]]
def graficar(vectores, proy1, proy2):
    plt.figure()
    for i in range(len(vectores)):
        # Vector original (azul)
        plt.quiver(0, 0, vectores[i][0], vectores[i][1], angles='xy', scale_units='xy', scale=1, color='blue')
        # Proyección sobre u1 (verde)
        plt.quiver(0, 0, proy1[i][0], proy1[i][1], angles='xy', scale_units='xy', scale=1, color='green')
        # Proyección sobre u2 (rojo)
        plt.quiver(0, 0, proy2[i][0], proy2[i][1], angles='xy', scale_units='xy', scale=1, color='red')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.show()
def main():
    u1 = vector_unitario_aleatorio()
    u2 = vector_unitario_aleatorio()
    originales, proy_u1, proy_u2 = [], [], []
    while True:
        v = leer_vector()
        originales.append(v)
        proy_u1.append(proyectar(v, u1))
        proy_u2.append(proyectar(v, u2))
        if input("¿Otro vector? (s/n): ").lower() != 's':
            break
    graficar(originales, proy_u1, proy_u2)
main()