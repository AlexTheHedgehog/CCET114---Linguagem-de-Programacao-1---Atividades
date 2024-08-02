valido = 0
notas = []
while valido < 2:
    nota = float(input())

    if 0 <= nota <= 10:
        valido += 1
        notas.append(nota)
    else:
        print('nota invalida')

media = (notas[0] + notas[1]) / 2
print(f'media = {media:.2f}')