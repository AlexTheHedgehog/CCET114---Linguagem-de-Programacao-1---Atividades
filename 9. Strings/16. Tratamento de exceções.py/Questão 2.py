import sys
"""O código abaixo contém bugs. Adicione uma cláusula try/except para que o código seja executado sem
erros. Se uma postagem de blog não obteve nenhum Like, uma chave 'Likes' deve ser adicionada a esse
dicionário com um valor de 0.
d=[{'Fotos':3,'Likes':21},{'Comentários':2,'Compartilhamentos':1}, {'Fotos':5,'Likes':33,'Comentários':8},{'Fotos':4,'Compartilhamentos':2}, {'Fotos':8,'Comentários':1}]
total_likes = 0
for post in d:
    total_likes = total_likes + post['Likes']
print(total_likes)"""


d = [{'Fotos':3,'Likes':21},{'Comentários':2,'Compartilhamentos':1}, {'Fotos':5,'Likes':33,'Comentários':8}, {'Fotos':4,'Compartilhamentos':2}, {'Fotos':8,'Comentários':1}]
total_likes = 0
for post in d:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0
    except:
        print(f'O erro foi {sys.exc_info()[0]}')
print(d) # para ver se a chave 'Likes' foi adicionada corretamente
print(total_likes)