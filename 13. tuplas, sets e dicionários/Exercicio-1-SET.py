# 1)Escreva um programa que receba duas listas com nomes de pessoas e determine:
# ● Quantas pessoas estão nas duas listas ao mesmo tempo
# ● Quantas pessoas duplicadas
# ● O total de pessoas distintas nas duas listas
# ● Quantas pessoas estão apenas em uma das duas listas

a, b = input().split()
lista1 = a.replace('[', '').replace(']', '').split(',')
lista2 = b.replace('[', '').replace(']', '').split(',')
set_1 = set(lista1); set_2 = set(lista2)

dup = 0
inter = set_1 & set_2
dist = set_1 ^ set_2
umadas_1 = set_1 - set_2
umadas_2 = set_2 - set_1

for i in set_1:
    if lista1.count(i) >= 2:
        dup += 1

for i in set_2:
    if lista2.count(i) >= 2:
        dup += 1

print(f'''Pessoas nas duas listas ao mesmo tempo: {len(inter)}
Pessoas duplicadas: {dup}
Pessoas distintas nas duas listas: {len(dist)}
Pessoas que estão em apenas uma das listas:\n   Lista1: {len(umadas_1)}\n   Lista2: {len(umadas_2)}''')