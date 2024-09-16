n = int(input())

frase = list(input().split())

for j in range(n):
    if len(frase[j]) == 3:
        if frase[j].startswith('OB'):
            frase[j] = 'OBI'
        if frase[j].startswith('UR'):
            frase[j] = 'URI'

resp = ' '.join(frase)

print(resp)