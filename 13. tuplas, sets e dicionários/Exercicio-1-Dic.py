# 1)Escreva um programa que transforma uma lista de
# tuplas em um dicionário que associa o primeiro
# componente de cada tupla ao segundo.

dic = {}
lista = []
a, b = input().split()
tupla1 = tuple(a.replace('(', '').replace(')', '').split(','))
tupla2 = tuple(b.replace('(', '').replace(')', '').split(','))

lista.append(tupla1); lista.append(tupla2)

if len(tupla1) == len(tupla2):
    for i in range(len(tupla1)):
        dic[tupla1[i]] = tupla2[i]
    
    print(dic)

else:
    print('ERRO! O tamanho das tuplas deve ser igual.')