x = 5

def altera_valor():
    global x
    x = 7
    print(f'O valor de x dentro da função: {x}')


print(f'O valor de x fora da função: {x}')
altera_valor()
print(f'O valor de x após a chamada da função: {x}')