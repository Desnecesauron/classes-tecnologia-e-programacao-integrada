# Crie um algoritmo para ler um arquivo texto


def read_file(file):
    with open(file, 'r') as f:
        return f.read()


print(read_file('arq.txt'))