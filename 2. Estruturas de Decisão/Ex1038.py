cod, quant = map(int, input().split())
valor = 0.0

if cod == 1:
    valor = 4.0 * quant
elif cod == 2:
    valor = 4.5 * quant
elif cod == 3:
    valor = 5.0 * quant
elif cod == 4:
    valor = 2.0 * quant
elif cod == 5:
    valor = 1.5 * quant

print(f'Total: R$ {valor:.2f}')