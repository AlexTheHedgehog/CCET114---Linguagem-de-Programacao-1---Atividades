n = int(input())
lista = {}

for i in range(n):
    maior = 0; maior_nome = ''
    x, y = map(int, input().split())
    
    lista['Rafael'] = (lambda a, b: (3*a)**2 + b**2) (x, y)
    lista['Beto'] = (lambda a, b: 2*(a**2) + (5*b)**2) (x, y)
    lista['Carlos'] = (lambda a, b: (-100)*a + b**3) (x, y)
    
    #for j, k in zip(lista.keys(), lista.values()):
    for j, k in lista.items():
        if k > maior:
            maior = k
            maior_nome = j
    
    print(f'{maior_nome} ganhou')