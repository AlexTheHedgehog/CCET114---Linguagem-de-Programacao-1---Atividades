notas = [0] * 100
cont = cont_maior = num_maior = 0
alunos = int(input())
notas_alunos = list(map(int, input().split()))

for i in range(alunos):
    notas[i] = notas_alunos[i]

for i in range(alunos):
    for j in range(i+1, alunos):
        if notas[i] == notas[j]:
            cont += 1
    
    if cont > cont_maior or (cont == cont_maior and num_maior < notas[i]):
        cont_maior = cont
        num_maior = notas[i]
    
    cont = 0

print(num_maior)