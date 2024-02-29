
'''
with open('exerc/dados.txt', 'r') as arquivo:
    linha = arquivo.readline()

    while linha:
        print(linha)
        linha = arquivo.readline()

    linhas = arquivo.readlines()

    for row in linhas:
        print(row)

'''

import pandas as pd

df = pd.read_csv('exerc/dados.txt', header=None, names=['Nome', 'Matrícula', 'Data'])

print(df)