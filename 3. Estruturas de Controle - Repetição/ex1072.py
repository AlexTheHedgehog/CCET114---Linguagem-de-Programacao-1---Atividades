n = int(input())
i = 1
dentro = fora = 0

while i <= n:
    x = int(input())

    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1
    
    i += 1
    
print(f'{dentro} in\n{fora} out')