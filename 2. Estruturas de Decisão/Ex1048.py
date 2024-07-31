salario = float(input())
reajuste = novo = 0
percentual = ''

if 0 <= salario <= 400:
    reajuste = (15/100) * salario
    percentual = '15 %'
elif 400.01 <= salario <= 800:
    reajuste = (12/100) * salario
    percentual = '12 %'
elif 800.01 <= salario <= 1200:
    reajuste = (10/100) * salario
    percentual = '10 %'
elif 1200.01 <= salario <= 2000:
    reajuste = (7/100) * salario
    percentual = '7 %'
elif salario >= 2000:
    reajuste = (4/100) * salario
    percentual = '4 %'

print(f'''Novo salario: {salario + reajuste:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: {percentual}''')