# num = int(input())
# contador

'''i = 1
while i <= num:
    print(i)
    i += 1'''

# acumulador

# indicador
# num = []
# while resp in 'Ss':
#     num.append(int(input()))
#     resp = input('Deseja continuar? [S/N]')

# num2 = num.copy()
# num2.sort()
# if num == num2:
#    print('Está em ordem crescente.')
# else:
#    print('Não está em ordem crescente.')

n = int(input())
i = 1
status = False

while i < n-1:
    if i == 0:
        ant = int(input())
    x = int(input())
    if x < ant:
        status = True
    ant = x

if status:
    print('crescente')
else:
    print('decrescente')