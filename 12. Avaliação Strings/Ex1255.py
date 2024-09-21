n = int(input())

for i in range(n):
    letras = []
    letras_maiores = []
    maior = 0
    frase = input().lower()

    for j in frase:
        if j.isalpha() and j not in letras:
            letras.append(j)
    for j in letras:
        aux = frase.count(j)
        if aux > maior:
            maior = aux
    for j in letras:
        if frase.count(j) == maior:
            letras_maiores.append(j)

    letras_maiores.sort()
    print(''.join(letras_maiores))