# Crie um algoritmo para ler dados de um CSV
# (que possui o nome de vendedores e o valor
# de cada venda realizada), retornando qual
# o vendedor que mais vendeu e o que menos vendeu

import csv
import os


def main():
    file = os.path.join(os.path.dirname(__file__), "data", "sales_complex.csv")
    with open(file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        vendas = {}
        for row in reader:
            if row[0] in vendas:
                vendas[row[0]] += float(row[1])
            else:
                vendas[row[0]] = float(row[1])
        vendedor_fera = max(vendas, key=vendas.get)
        vendedor_lixo = min(vendas, key=vendas.get)
        print(f'O vendedor que mais vendeu foi {vendedor_fera}')
        print(f'O vendedor que menos vendeu foi {vendedor_lixo}')
        return [vendedor_fera, vendedor_lixo]


max_mix = main()
print(max_mix)