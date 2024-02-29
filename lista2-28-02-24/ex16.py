# Crie um algoritmo para consolidar um ou mais
# arquivos de texto de um diretório

import os
import csv


def consolidate_files(directory):
    files = os.listdir(directory)
    print(files)
    consolidated = []
    for file in files:
        with open(directory + "\\" + file) as f:
            reader = csv.reader(f)
            for row in reader:
                consolidated.append(row)
    return consolidated


def exclude_file_if_exists(file):
    if os.path.exists(file):
        os.remove(file)


def write_file(data):
    with open("C:\\Users\\cesin\\PycharmProjects\\classes-tecnologia-e-programacao-integrada\\lista2-28-02-24\\data\\consolidated.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(arrSomeFile)


arrSomeFile =consolidate_files("C:\\Users\\cesin\\PycharmProjects\\classes-tecnologia-e-programacao-integrada\\lista2-28-02-24\\data")
print(arrSomeFile)
exclude_file_if_exists("C:\\Users\\cesin\\PycharmProjects\\classes-tecnologia-e-programacao-integrada\\lista2-28-02-24\\data\\consolidated.csv")
write_file(arrSomeFile)
