# Crie um algoritmo para ler um arquivo JSON

import json


def read_json(filename='arq.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
        print(data)
        print(type(data))
        print(data['nome'])
        print(data['idade'])
        print(data['cidade'])
        for item in data['carros']:
            print(item)


read_json()