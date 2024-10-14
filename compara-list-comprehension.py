from time import time
#CUIDADO AO RODAR ESSE PROGRAMA, É PRA TESTAR CONSUMO ALTO DE MEMÓRIA

#função de loop interativo
tamanho = 10**7
def loop(t):
    lista = []
    for i in range(t):
        lista.append(i*i)
    return lista

#função com list comprehension
def listc(t):
    lista = [i*i for i in range(t)]
    return lista

def gera(t):
    for i in range(t):
        yield (i*i)

inicio = time()
loop(tamanho)
fim = time()
tempo = round(fim - inicio, 2)
print(tempo)

inicio = time()
listc(tamanho)
fim = time()
tempo = round(fim - inicio, 2)
print(tempo)

inicio = time()
for i in gera(tamanho):
    continue
fim = time()
tempo = round(fim - inicio, 2)
print(tempo)