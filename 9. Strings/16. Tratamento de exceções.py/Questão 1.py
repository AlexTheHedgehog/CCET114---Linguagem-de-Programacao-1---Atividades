import sys
"""1. O código abaixo atribui a 4a letra de cada palavra em comida ao quinto da nova lista. No entanto, o
código atualmente produz erros. Insira uma cláusula try/except que permitirá que o código seja executado e
produza uma lista da 4a letra de cada palavra. Se a palavra não for longa o suficiente, não deve fazer nada.
palavras = ['inefável', 'grill', 'faz', 'batata', 'ruim', '.', 'A', 'exceção', 'é',
'quando', 'faz', 'um', 'salgado', 'saboroso']
palavra = []
for x in palavras:
    palavra.append(x[3])
print(''.join(palavra))"""
palavras = ['inefável', 'grill', 'faz', 'batata', 'ruim', '.', 'A', 'exceção', 'é', 'quando', 'faz', 'um', 'salgado', 'saboroso']
palavra = []
for x in palavras:
    try:
        palavra.append(x[3])
    except IndexError:
        pass
    except:
        print(f'O erro foi {sys.exc_info()[0]}')

print(''.join(palavra))