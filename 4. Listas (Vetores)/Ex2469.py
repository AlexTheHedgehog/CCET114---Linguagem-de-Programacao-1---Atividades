alunos = int(input())
notas = list(map(int, input().split()))
frequente = [0, 0]
for i in notas:
    vezes = notas.count(i)
    if vezes > frequente[1] or (vezes == frequente[1] and i > frequente[0]):
        frequente[1] = vezes
        frequente[0] = i

print(frequente[0])