# Escreva um programa que substitua todas as
# ocorrências de uma letra em uma string por outra letra

def replaceLetter(s, old, new):
    newString = ''
    for c in s:
        if c == old:
            newString += new
        else:
            newString += c
    return newString

abc= 'abeeeeeeec'
print(replaceLetter(abc, 'e', 'x')) # abxxxxxxxc