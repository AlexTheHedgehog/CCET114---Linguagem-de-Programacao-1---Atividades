renda = float(input())

if 0 <= renda <= 2000:
    print('Isento')
elif 2000.01 <= renda <= 3000:
    print(f'R$ {((8/100)*renda):.2f}')
elif 3000.01 <= renda <= 4500:
    print(f'R$ {((18/100)*renda):.2f}')
else:
    print(f'R$ {((28/100)*renda):.2f}')