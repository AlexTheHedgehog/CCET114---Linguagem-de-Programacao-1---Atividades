# questão a) 30%
def primos():
    for cont in range(1, 10001):
        div = 0
        for i in range(1, cont+1):
            if cont // i != 0:
                div += 1

        if div == 2 and cont != 1:
            yield cont

primos_iterado = iter(primos())
print(next(primos_iterado))
print(next(primos_iterado))
print(next(primos_iterado))