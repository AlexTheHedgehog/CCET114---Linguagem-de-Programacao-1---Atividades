# 3)Escreva um programa que conta a quantidade de
# vogais em um string e armazena tal quantidade em um
# dicionário, onde a chave é a vogal considerada.

frase = input('Entre com uma frase ou palavra: ').lower()
dic = {}

for i in 'aeiou':
    if i in frase:
        dic[i] = frase.count(i)

for i in dic.keys():
    print(f'Quantidade da vogal {i} = {dic[i]}')