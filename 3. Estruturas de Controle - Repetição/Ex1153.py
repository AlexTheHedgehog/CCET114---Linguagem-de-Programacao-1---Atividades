n = int(input())
fatorial = n
while n > 1:
    fatorial *= n-1
    n -= 1

print(fatorial)