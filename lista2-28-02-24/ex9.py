# Escreva um programa que encontre o par de elementos
# em uma lista cuja soma seja igual a um determinado valor

def findPair(l, s):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == s:
                return (l[i], l[j])
    return None

abc= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(findPair(abc, 10)) # (1, 9)
print(findPair(abc, 23)) # None