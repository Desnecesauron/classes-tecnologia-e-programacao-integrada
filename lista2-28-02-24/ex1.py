# crie uma função que conte o número de vogais em uma string.

def countVogals(s):
    vogals = 'aeiou'
    count = 0
    for c in s:
        if c in vogals:
            count += 1
    return count

abc= 'abeeeeeeec'
print(countVogals(abc)) # 8