# Crie uma função que conte o número de ocorrências
# de uma determinada palavra em uma frase.

def countWord(s, word):
    return s.split().count(word)

abc= 'ab eeeeee ab c'
print(countWord(abc, 'ab')) # 2