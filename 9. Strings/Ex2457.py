letra = input().lower()
frase = list(input().lower().split())
cont = 0
for i in frase:
    if letra in i:
        cont += 1

porc = (cont / len(frase)) * 100

print(f'{porc:.1f}')