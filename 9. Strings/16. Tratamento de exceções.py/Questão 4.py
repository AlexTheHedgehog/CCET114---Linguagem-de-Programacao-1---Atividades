import sys
# Escreva um programa que leia um valor real do teclado armazenando-o em uma variável do tipo float. Se
# o usuário digitar um valor que não possa ser convertido em um valor do tipo float, seu programa deve
# solicitar ao usuário que digite um novo valor. Se o usuário não digitar um valor aceitável por três vezes, seu
# programa deve terminar imprimindo a mensagem “Você excedeu o limite de tentativas.”.

count = 0
while True:
    try:
        num = float(input('Insira um valor real: '))
        print('AEEE, CONSEGUIU!')
        break
    except ValueError:
        count += 1
        if count == 3:
            print('Você excedeu o limite de tentativas.')
            break
        else:
            print(f'O valor inserido não pode ser convertido para float. Tente novamente!')
    except:
        print(f'O erro foi {sys.exc_info()[0]}')
