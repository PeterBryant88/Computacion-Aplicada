#PROBLEMA
# Material I      A + 3 B  = 300
# Material II 1.5 A + 2 B = 350

import numpy as np

# Arreglos de los coeficientes del sistema
A = np.array([[1, 3], [1.5, 2]])
B = np.array([300, 350])

# Cálculo de las soluciones
X = np.linalg.solve(A, B)

print("Soluciones del sistema:")
print("A =", round(X[0], 3))
print("B =", round(X[1], 3))