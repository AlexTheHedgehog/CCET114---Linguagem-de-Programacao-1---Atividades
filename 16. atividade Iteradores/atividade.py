from random import randint
# 1) Crie uma função geradora para a série e imprima no formato lista: [(0, 2), (1, 3), (2, 4), (4, 6), (5, 7)]
geradora = ((i, i+2) for i in range(6))
print(list(geradora))

# 2) Desenvolva uma função geradora para imprimir uma sequência infinita de números
def inf():
    n = 0
    while True:
        yield print(n, end=' ')
        n += 1

seq_inf = iter(inf())

for i in range(20): #funciona com qualquer valor
    next(seq_inf)
print()

# 3) Defina uma função geradora para imprimir 6 números (entre 1 e 60) da mega sena (use randint para gerar os números aleatórios)
geradora = (print(randint(1, 60), end=' ') for i in range(6))
for i in geradora:
    i
print()

# 4) Crie uma função geradora para somar os valores de cada tupla numérica contida
#    em uma lista e imprima os somatórios. Entrada: [(1, 2, 3), (5, 7), (99, 15, -5)]
#    Saída: 6 12 109
entrada = '[(1, 2, 3), (5, 7), (99, 15, -5)]'
geradora = (sum(i) for i in eval(entrada))

for i in geradora:
    print(i, end=' ')
print()

# 5) Implemente uma função que recebe um iterator e retorna os elementos sem
#    repetições do mesmo elemento em sequencia. Entrada: 'aaabbacabbbd' Saída:
#    ['a', 'b', 'a', 'c', 'a', 'b', 'd']
entrada = 'aaabbacabbbd'
geradora = (entrada[i] for i in range(len(entrada)) if entrada[i-1] != entrada[i])
print(list(geradora))

# 6) Qual a diferença de desempenho entre as expressões? Uma expressão é
#    preferível à outra? Por quê?
#    1) sum(1/n for n in range(1, 10**7))
#    2) sum([1/n for n in range(1, 10**7)])
# Resposta: a expressão nº 1), pois ela é uma função geradora, portanto o espaço na memória não é totalmente utilizado,
# apenas tem acesso aos endereços desses valores.