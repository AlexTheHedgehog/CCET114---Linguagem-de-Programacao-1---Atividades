algarismos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
valor = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
soma = 0
n = int(input())

for i in range(n):
    v = list(map(int, list(input())))

    for j in range(len(v)):
        indice = algarismos.index(v[j])
        soma += valor[indice]

    print(f'{soma} leds')
    soma = 0