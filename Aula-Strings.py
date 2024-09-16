# Strings são imutáveis
# Join() faz ela ser mutável

L = list('Alô Mundo')
L[0] = 'a'
print(L) #['a','l','ô',' ','M','u','n','d','o']
str = ''.join(L)
print(str)

# find(sub_string_procurada, pos_inicio, pos_fim)
# Retorna a posição do índice da primeira ocorrência
# da substring procurada na String que está sendo consultada.
# se não encontrar, retorna -1

nome = "Manoel Limeira de Lima"
i = nome.find("Limeira")
print(i) # escreve 7

i = nome.find("a")
print(i) # escreve 1

i = nome.find("a", 7, len(nome))
print(i) # escreve 13

'Lima' in nome #True