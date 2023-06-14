import numpy as np
import matplotlib.pyplot as plt

from population import *
from gray2real import *
from fitness import *
from selection import *
from crossover import *
from mutation import *
from newindiv import *

def main():

    # Crear población inicial
    n = 32  # tamaño de la población
    g_len = 8  # 10 bits por variable
    c_len = 32  # Variables de 10 bits cada una
    pop = population(n, c_len)  # Población inicial

    print("G_A")
    print("Tamaño de población : \t", n, "individuos")
    print("Tamaño de cromosoma : \t", c_len, "bits")
    # print("Población inicial : \t", pop)

    bestfitg = []
    tg = int(input("Cantidad total de generaciones: "))

    for g in range(0, tg):
        fit = []
        for indiv in pop:
            fit.append(fitness(gray2real(indiv)))
        #print("fit: ", fit)
        #print("max fit: ", np.max(fit))
        #print("min fit: ", np.min(fit))
        #print("mean fit: ", np.mean(fit))
        #print("std fitness: ", np.std(fit))

        fit_index = selection(fit)
        parent0 = pop[fit_index]
        #print("p0: ",fit_index)  # Debug

        #print("fit_index: ", fit_index)
        #print(parent0)
        #print(pop[fit_index])

        fit_index = selection(fit)
        parent1 = pop[fit_index]
        #print("p1: ",fit_index)  # Debug

        while parent1 == parent0:
            fit_index = selection(fit)
            parent1 = pop[fit_index]
            # print("p12: ", fit_index) # Debug

        ###print("par0: ", parent0) # Debug
        ###print("par1: ", parent1) # Debug

        offspring0, offspring1 = crossover(parent0, parent1)  # Crossover

        offspring0 = mutation(offspring0)
        offspring1 = mutation(offspring1)

        ###print("off0: ", offspring0)
        ###print("off1: ", offspring1)

        fitp0 = fitness(gray2real(parent0))
        fitp1 = fitness(gray2real(parent1))
        fito0 = fitness(gray2real(offspring0))
        fito1 = fitness(gray2real(offspring1))

        ###print("fit_par0: ", fitp0)
        ###print("fit_par1: ", fitp1)
        ###print("fit_off0: ", fito0)
        ###print("fit_off1: ", fito1)

        newpop = []
        if fito0 >= fitp0 or fito0 >= fitp1:
            newpop.append(offspring0)
        if fito1 >= fitp0 or fito1 >= fitp1:
            newpop.append(offspring1)
        if fitp0 >= fito0 or fitp0 >= fito1:
            newpop.append(parent0)
        if fitp1 >= fito0 or fitp1 >= fito1:
            newpop.append(parent1)

        # Elitismo (Incluir al mejor(es) individuo(s))

        bestfit = np.max(fit)
        bestfitg.append(1 / bestfit)
        bestindex = fit.index(bestfit)
        newpop.append(pop[bestindex])

        # Elitismo extendido
        meanfit = np.mean(fit)
        stddevfit = np.std(fit)
        for i in range(len(fit)):
            if fit[i] > meanfit + stddevfit:
                newpop.append(pop[i])

        # Fillers (relleno)
        while (len(newpop) < n):
            newpop.append(newindiv(c_len))

        pop = newpop

    bestfit = np.max(fit)
    bestindex = fit.index(bestfit)
    sol = gray2real(pop[bestindex])
    print(f"W: {round(sol[0], 1)}μm L: {round(sol[1], 1)}μm  m: {sol[2]} n: {sol[3]}")
    plt.figure(1)
    plt.plot(bestfitg)
    plt.show()

main()