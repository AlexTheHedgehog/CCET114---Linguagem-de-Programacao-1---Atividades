n = int(input())

for i in range(n):
    indice = 2
    ra = input()
    for j in range(20):
        if 2 <= j <= 19 and ra[j] != '0':
            indice = j
            break

    if len(ra) == 20 and ra.startswith('RA'):
        print(ra[indice:])
    else:
        print('INVALID DATA')