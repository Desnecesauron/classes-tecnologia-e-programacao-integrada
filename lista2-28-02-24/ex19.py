# Crie um algoritmo para ler dados de um CSV
# (que possui o nome de vendedores e o valor
# de cada venda realizada), retornando qual
# a soma de vendas que teve cada vendedor

import csv
import os
from collections import defaultdict


def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
    return header, data


def sales_by_seller(data):
    sales = defaultdict(float)
    for seller, value in data:
        sales[seller] += float(value)
    return sales


def main():
    file = os.path.join(os.path.dirname(__file__), "data", "sales_complex.csv")
    header, data = read_csv(file)
    sales = sales_by_seller(data)
    print(sales)


main()