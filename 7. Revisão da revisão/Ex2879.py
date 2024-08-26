n = int(input())
carro = 0
for i in range(n):
    porta = int(input())
    if porta != 1:
        carro += 1

print(carro)