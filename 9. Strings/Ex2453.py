frase = list(input().split())
resp = ''

for i in frase:
    for j in range(1, len(i), 2):
        resp += i[j]
    resp += ' '
print(resp[:-1])