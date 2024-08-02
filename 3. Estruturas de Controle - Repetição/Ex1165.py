casos = int(input())
i = 1

while i <= casos:
    j = 1
    div = 0
    num = int(input())

    while j <= num:
        if num % j == 0:
            div += 1
        
        j += 1
        
    if div == 2:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')

    i += 1