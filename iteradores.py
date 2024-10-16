#criar um iterador
iterador = iter('ABC')
print(next(iterador), next(iterador), next(iterador))
#qualquer iterável pode ser percorrido com laço
for i in iterador:
    print(i)
#a função next só funciona em iterators
#next(str)
#função que retorna iterador
alunos = ['Daniel', 'Juan', 'Gustavo']
it = enumerate(alunos) #o retorno é um iterador
#print(next(it))
reverso = reversed(alunos)
for i in reverso:
    print(i)
#criar um dicionário a partir de um iterador
dicionario = dict(it)
print(dicionario)

numeros = [1,2,3,4]
geradora = (i**2 for i in numeros)
combinacao = zip(numeros, geradora)
for i, j in combinacao:
    print(i, j)