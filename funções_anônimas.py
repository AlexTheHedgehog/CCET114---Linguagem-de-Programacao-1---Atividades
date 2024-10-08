from functools import reduce

# Uma empresa lhe contratou para processar as
# faturas de cartão de crédito que estão
# organizadas em uma lista de tuplas

# Vc precisa manipular essas informações para:
# – Imprimir no formato ‘Tipo de gasto’ – R$ valor
# – Ordenar os itens por valor
# – Filtrar os gastos acima de R$ 500
# – Apresentar o total da fatura

fatura = [('Net', 199.9),('Ifood', 999.87),('Gasolina', 678.0),('Formigão', 400)]

print('\n'.join(map(lambda x: f'{x[0]} - R${x[1]}', fatura)))
fatura.sort(key = lambda x: x[1], reverse=False)
print(fatura)
maiores = list(filter(lambda x: x[1] > 500, fatura))
print(maiores)
#total = reduce(lambda x, y: x[1]+y[1], fatura)
total = reduce(lambda x,y: x+y, list(dict(fatura).values()))
print(total)