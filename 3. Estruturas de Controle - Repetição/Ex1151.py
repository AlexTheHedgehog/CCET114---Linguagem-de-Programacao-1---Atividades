n = int(input())
i = 1
ant1 = 0
ant2 = 1

while i <= n:
    if i == 1:
        print('0', end='')
    elif i == 2:
        print(' 1', end='')
    else:
        num = ant1 + ant2
        if i == n:
            print(f' {num}')
        else:
            print(f' {num}', end='')

        ant1 = ant2
        ant2 = num
    
    i += 1