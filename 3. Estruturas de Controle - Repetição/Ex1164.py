casos = int(input())
i = 1

while i <= casos:
    j = 1
    soma = 0
    num = int(input())

    while j < num:
        if num % j == 0:
            soma += j
        
        j += 1
        
    if soma == num:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')

    i += 1