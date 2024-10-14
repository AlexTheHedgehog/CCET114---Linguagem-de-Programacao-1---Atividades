num = [1,2,3,4,5,6,7,8,9,10]
#Nova lista com elementos ao quadrado
quad = [i*i for i in num]
print(quad)
#Lista apenas com os números pares
pares = [i for i in num if i%2==0]
print(pares)
#Lista com pares quadrados e ímpares
lista = [i if i%2==0 else i*i for i in num]
print(lista)
#Lista com combinação de letras e números
let = ['a','b','c']
num = [1,2,3]
com = [(l,n) for l in let for n in num]
print(com)
#Lista com combinação de números e letras
com = [[l,n] for n in num for l in let]
print(com)
#Gerando matriz de tamanho 3x4
mat = [[j+1+i*4 for j in range(4)] for i in range(3)]
print(mat)
#Transposta
#mat_t = []
#for i in range(4):
#    linha = []
#    for j in range(3):
#        linha.append(mat[j][i])
#    mat_t.append(linha)
#print(mat_t)
#Modo list-comprehension
mat_t = [[i+1+j*4 for j in range(3)] for i in range(4)]
print(mat_t)
#Usando strings
frutas = [' abacate', ' banana ', 'abacaxi ']
novas_frutas = [fruta.strip().upper() for fruta in frutas]
print(novas_frutas)
#Com conjuntos (sets)
frase = 'Estou extremamente exausto da rotina socorro'
vogais_todas = [i for i in frase if i in 'aeiou']
vogais_unicas = {i for i in frase if i in 'aeiou'}
print(vogais_todas)
print(vogais_unicas)
#Com dicionários
vogais_dict = {i:i.upper() for i in frase if i in 'aeiou'}
#Exemplo para criar uma função geradora
num = [1,2,3,4,5,6,7,8,9,10]
geradora = (i*i for i in num)
print(geradora)
for g in geradora:
    print(g)