lista = ['b', 'a', 'n', 'a', 'n', 'a']
tam = lista.count('a')

for i in range(tam):
    lista.remove('a')
print(lista)