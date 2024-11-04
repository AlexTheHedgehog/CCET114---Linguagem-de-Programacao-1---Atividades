#A média deveria ser 9.0
#90%
from functools import reduce
# questao a)
n = [10,20,30,40,50,60,70,80]; s = ['A','B','C','D','E','F','G','H']
segundo_primeiro = [(j, i) for i, j in zip(n, s)]
print(segundo_primeiro)

# questao b)
s = ['omo', 'lava', 'melhor', 'que', 'esse', 'ypê']
palindromos = list(filter(lambda x: x == x[::-1], s))
print(palindromos)

# questao c)
d = {'A1':{'Tipo':'Gato', 'Nome':'Bill', 'Idade':3}, 'A2':{'Tipo':'Cachorro', 'Nome':'Toby', 'Idade':8}, 'A3':{'Tipo':'Cachorro', 'Nome':'Shelby', 'Idade':10}}
media = reduce(lambda x, y: x+y, [i['Idade'] for i in d.values()]) / len(d)
print(media)