# Escreva um programa que implemente a soma
# de matrizes usando listas aninhadas

def sumMatrix(m1, m2):
    result = []
    for i in range(len(m1)):
        line = []
        for j in range(len(m1[i])):
            line.append(m1[i][j] + m2[i][j])
        result.append(line)
    return result

m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print(sumMatrix(m1, m2)) # [[6, 8], [10, 12]]