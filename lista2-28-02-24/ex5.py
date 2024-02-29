# Crie uma função que encontre os k maiores elementos
# em uma lista, mantendo a ordem original

def kMax(l, k):
    lAux = l.copy()
    lAux.sort(reverse=True)
    return l[:k]

abc= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(kMax(abc, 3)) # [10, 9, 8]
print(abc)
