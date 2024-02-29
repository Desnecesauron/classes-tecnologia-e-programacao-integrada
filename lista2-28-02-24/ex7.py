# Crie uma função que encontre a interseção
# de duas listas sem usar conjuntos

def intersection(l1, l2):
    l = []
    for e in l1:
        if e in l2 and e not in l:
            l.append(e)
    return l

abc= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
xyz= [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(intersection(abc, xyz)) # [5, 6, 7, 8, 9, 10]