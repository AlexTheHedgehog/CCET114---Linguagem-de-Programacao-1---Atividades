def fat(n):
    #ant = n
    if n == 0:
        return 1
    else:
        fatorial = n * fat(n-1)
        '''while n > 0:
            n -= 1
            fatorial = n * ant
            ant = n'''
        return fatorial
    
def fib(n):
    if 1 <= n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#Parâmetros: uma função e um inteiro
def soma(funcao, inteiro):
    total = 0
    for i in range(inteiro):
        total += funcao(i)
    return total

#Programa principal
soma(fat, 3)