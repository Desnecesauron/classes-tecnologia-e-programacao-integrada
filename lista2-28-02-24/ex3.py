# crie uma função que retorne o número de palavras em uma string

def countWords(s):
    return len(s.split())

abc= 'ab eeeeee c'
print(countWords(abc)) # 3