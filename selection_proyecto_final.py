import random
import numpy as np

def selection(fit):

    offset = abs(np.min(fit)) # Offset
    total_fit = (len(fit)*offset) + sum(fit) # Suma total de aptitudes
    pick = random.random() # No. aleatorio entre 0 y 1
    fit_p = [] # Proporción de aptitud respecto al total
    for i in range (0,len(fit)):
        fit_p.append(((fit[i]+offset)/total_fit))
    fit_acc = 0
    for i in range(0, len(fit)):
        fit_acc += fit_p[i]
        if fit_acc >= pick:
            fit_index = i
            break
    return fit_index
