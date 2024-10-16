frase = 'Teste de frase para funcionar nas questões, ebaaaa \(^-^\)'
numeros = [i for i in range(1, 21)]
# 1) Crie uma lista dos quadrados de todos os números ímpares entre 1 e 10.
quad_impar = [i**2 for i in range(1, 11) if i % 2 != 0]
print(quad_impar)

# 2) Listar todos os números de 1 a 107 que tenham o digito 7.
dig_7 = [i for i in range(1, 108) if '7' in str(i)]
print(dig_7)

# 3) Contar o número de espaços em branco de uma frase.
espacos = [i for i in frase if i == ' ']
print(espacos)
print(f'{len(espacos)} espaços em branco.')

# 4) Crie uma lista de todas as consoantes de uma frase.
consoantes = [i for i in frase if i not in 'aeiouAEIOU' and i.isalpha()]
print(consoantes)
print(f'{len(consoantes)} consoantes.')

# 5) Dada uma lista de temperaturas em graus Celsius, crie uma lista correspondente com as temperaturas em Fahrenheit (use a fórmula F = C * 9/5 + 32).
temperaturas = [100.0, 25.5, 14.0, 17.3, 20.95]
farenheit = [i * (9/5) + 32 for i in temperaturas]
print(farenheit)

# 6) Crie uma list comprehension que filtre todos os números primos de uma lista de números.
def is_primo(num):
    div = 0
    for d in range(1, num+1):
        if num % d == 0:
            div += 1
    
    if div == 2:
        return True
    else:
        return False

primos = [i for i in numeros if is_primo(i)]
print(primos)

# 7) Dada uma string, crie uma list comprehension que remova todas as vogais da string.
sem_vogais = [i for i in frase if i not in 'aeiouAEIOU']
print(sem_vogais)
print(''.join(sem_vogais))

# 8) Crie uma list comprehension que gere a tabuada do 7.
tabuada_7 = [i*7 for i in range(1, 11)]
print(tabuada_7)

# 9) Use list comprehension para calcular o produto de duas matrizes 2x2.
matriz_1 = [[1, 2],
            [3, 4]]
matriz_2 = [[6, 5],
            [9, 2]]
produto = [[sum(matriz_1[i][k] * matriz_2[k][j] for k in range(2)) for i in range(2)] for j in range(2)]
print(produto)

# 10) Dada uma lista de palavras, crie uma list comprehension que gere uma lista contendo apenas as palavras que são anagramas de uma palavra fornecida.
palavras = ['um', 'bocado', 'de', 'coisas', 'pra', 'arp', 'fazer', 'socorro', 'mu', 'bodoca', 'undertale', 'mario', 'sonic', 'mostarda', 'marrocos']
fornecida = input('Forneça uma palavra: ')
anagramas = [i for i in palavras if sorted(i) == sorted(fornecida)]
print(anagramas)

# 11) Quais as diferenças entre laços iterativos, list-comprehension e expressões(funções) geradoras na criação de listas?

# Resposta: laços iterativo demandam maior complexidade de uso de outras funções ou contextos de código;
# list comprehension serve para resumir laços que não demandam de tanta complexidade em uma única linha;
# expressões e funções são utilizadas para calcular o valor que o laço retornará como elemento da lista.