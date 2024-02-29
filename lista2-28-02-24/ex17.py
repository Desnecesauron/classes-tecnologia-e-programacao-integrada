# Crie um algoritmo para ler dados de um CSV
# (que possui os meses e valores de vendas),
# retornando qual o mês teve mais vendas

import csv
import os


def read_file(file):
    with open(file) as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data


def month_with_most_sales(data):
    sales = {}
    for row in data:
        month = row[0]
        value = float(row[1])
        if month in sales:
            sales[month] += value
        else:
            sales[month] = value
    return max(sales, key=sales.get)


def main():
    file = os.path.join(os.path.dirname(__file__), "data", "sales.csv")
    data = read_file(file)
    print(month_with_most_sales(data))


main()
