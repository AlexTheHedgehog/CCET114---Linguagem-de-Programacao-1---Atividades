alfabeto = list(map(chr, range(97, 123)))
n = int(input())

for i in range(n):
    letras = []
    frase = input().lower()

    for j in frase:
        if j in alfabeto and j not in letras:
            letras.append(j)
            
    if len(letras) == len(alfabeto):
        print('frase completa')
    elif len(letras) < len(alfabeto)/2:
        print('frase mal elaborada')
    else:
        print('frase quase completa')