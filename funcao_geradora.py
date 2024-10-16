def imprimir():
    print('Imprime 1')
    yield 1
    print('Imprime 2')
    yield 2
    print('Imprime 3')
    yield 3

it = imprimir() #o retorno da função geradora é um iterador

print(next(it), next(it), next(it))

def geradora():
    for i in range(10):
        yield i

it = geradora()
while True:
    try:
        print(next(it))
    except StopIteration:
        break