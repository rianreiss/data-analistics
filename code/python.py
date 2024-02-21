import csv

# objetivo: imprimir as primeiras 10 linhas do dataset para fins de visualização.
# utilizando a coluna ID (regularmente tratada) como base.

# abrindo em modo 'read'
with open('./dataset/apple_quality.csv', 'r') as csvfile:
    # objeto para leitura
    reader = csv.reader(csvfile)

    # pulando o cabeçalho
    next(reader)

    # imprimindo apenas as primeiras 10 linhas do arquivo
    for row in reader:
        if int(row[0]) < 10:  # comparação com base no valor do ID, convertido em inteiro.
            print(', '.join(row))  # imprime os dados da linha separados por vírgula
            # em formato de lista: print(row)
        else:
            break  # quebra quando o ID chega em 10