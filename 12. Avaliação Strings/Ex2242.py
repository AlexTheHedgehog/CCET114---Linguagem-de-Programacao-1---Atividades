risada = input().lower()
vogais = []
for i in risada:
    if i in 'aeiou':
        vogais.append(i)

vogais_reverso = vogais.copy()
vogais_reverso.reverse()

if vogais == vogais_reverso:
    print('S')
else:
    print('N')