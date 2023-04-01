#PROBLEMA
# Material I      A + 3 B  = 300
# Material II 1.5 A + 2 B = 350

import numpy as np

# Entrada de usuario, # de incógnitas
n = int(input('Introduce el número de incógnitas: '))

# Arreglo de ceros para la matriz aumentada A:B
ab = np.zeros((n, n+1))

# Lectura de coeficientes de la matriz A:B
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        ab[i][j] = float(input('A:B['+ str(i)+']['+str(j)+']='))
print("Ax = b: \n", ab)

# Matriz Delta de ceros
D = np.zeros((n,n))
# Arreglo de ceros de las n soluciones
x = np.zeros(n)

# Cálculo del determinante Delta
det_D = np.linalg.det(ab[:,:n])

# Cálculo del determinante Delta n
for c in range(n):
    # Matriz Delta n
    D = np.copy(ab[:,:n])
    D[:,c] = ab[:,n]
    det_Dn = np.linalg.det(D)
    # Cálculo de las soluciones
    x[c] = det_Dn/det_D

print("Soluciones del sistema:")
for i in range(n):
    print("X",i+1,"=",round(x[i],3))