import numpy as np
#Se importa la libreria "numpy" en orden de crear la matriz y luego evaluarla
A=np.array([
    [0.0579,.24,.214],
    [.143,.494,.511],
    [.679,.227,.20]
])
#Se crea la matriz con el contenido nutricional de los ingredientes
B=np.array([31,65,55])
#Se crea otra matriz que será
print(np.linalg.solve(A,B))
#Se imprimen los valores de X Y y Z
