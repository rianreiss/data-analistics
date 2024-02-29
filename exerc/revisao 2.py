
# Saída de dados
print("Olá, mundo!")

# Variáveis
mensagem = "Olá, python!"
print(mensagem)

# Tipos de dados
inteiro = 10
floatType = 3.1415
string = 'Bolacha'
boolean = True

# Operações
soma = inteiro + floatType

print(soma)

# Entrada de dados
nome = input('Digite seu nome: ')
print(nome)

# Estrutura de decisão e repetição
idade = int(input(nome + ', qual a sua idade? '))

if idade < 18:
    print('Você é menor de idade, fique em paz...')
else:
    print('Você é maior de idade. kkjj')

for i in range(5):
    print('ha')

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Listas
frutas = ['maca', 'banana', 'uva']

for x in frutas:
    print(x)

# Funções
def saudacoes(nome):
    print('Olá '+ nome + '. Td bem?')

saudacoes('Rian')