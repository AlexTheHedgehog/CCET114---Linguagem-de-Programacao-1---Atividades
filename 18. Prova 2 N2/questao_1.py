#Letra 'a' deveria fazer a contagem das vogais
#Letra d deveria fazer com um set
#Letras b,c,e corretas
#90%
lista = ['A educação', 'é a arma', 'mais poderosa', 'que você', 'pode', 'usar','para', 'mudar o mundo']
print(f'Lista de entrada: {lista}')

# questão a)
vogais = [i for i in ' '.join(lista) if i in 'AEIOUaeiouÁÃÂÀÉÊÍÓÕÔÚáãâàéêíóõôú']
print(vogais)

# questão b)
palavras_maiq6 = tuple(i for i in list((' '.join(lista)).split()) if len(i) > 6)
print(palavras_maiq6)

# questão c)
total_chr_esp = [(len(i.replace(' ', '')), i.count(' ')) for i in lista]
print(total_chr_esp)

# questao d)
consoantes = [i for i in ' '.join(lista) if i not in 'AEIOUaeiouÁÃÂÀÉÊÍÓÕÔÚáãâàéêíóõôú ']
print(consoantes)

# questao e)
quant_chr = {i: ' '.join(lista).count(i) for i in ' '.join(lista) if i != ' '}
print(quant_chr)