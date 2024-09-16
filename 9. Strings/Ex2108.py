maior = ''
while True:
    x = input()
    if x == '0':
        break
    frase = list(x.split())
    for i in range(len(frase)):
        if i < len(frase)-1:
            print(f'{len(frase[i])}-', end='')
        else:
            print(f'{len(frase[i])}')
        if len(frase[i]) >= len(maior):
            maior = frase[i]

print(f'\nThe biggest word: {maior}')