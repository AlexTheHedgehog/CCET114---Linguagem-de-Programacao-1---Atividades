# 2)Escreva um programa que transforma um dicionário
# em uma lista de tuplas, onde as tuplas são ordenadas
# pelo primeiro componente. Lembre-se da função sort().

dic = {}
n = int(input('Quantidade de itens no dicionário: '))   #Lendo o dicionário

for i in range(n):
    a, b = input().split(':')   #Exemplo de entrada: "Ano:2024"
    dic[a] = b

lista1 = list(dic.keys())
lista2 = list(dic.values())
lista1.sort(); lista2.sort()
tupla1 = tuple(lista1)
tupla2 = tuple(lista2)

print(tupla1, tupla2)