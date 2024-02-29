# Crie uma função que embaralhe os elementos
# de uma lista de forma aleatória

import random

def shuffleList(l):
    lAux = l.copy()
    random.shuffle(lAux)
    return lAux

abc= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffleList(abc))