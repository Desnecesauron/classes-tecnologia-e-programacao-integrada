# Crie um algoritmo para ler um arquivo CSV

import csv

def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


read_csv('arq.csv')