import random

def mutation(indiv):

    if random.random() < 0.05: # Mutation index
        x = random.randint(0,len(indiv)-1)
        ###print("Mutation @", x)
        if indiv[x] == 1:
            indiv[x] = 0
        else:
            indiv[x] = 1
    ###else:
        ###print("No mutation")

    return indiv