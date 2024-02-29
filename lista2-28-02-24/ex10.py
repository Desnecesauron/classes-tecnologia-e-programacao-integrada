# Criar um algoritmo para calcular a frequência
# que uma palavra aparece em um texto

def wordFrequency(text, word):
    return text.split().count(word)

text = "O rato roeu a roupa do rei de Roma"
print(wordFrequency(text, "rato")) # 1
print(wordFrequency(text, "rei")) # 1