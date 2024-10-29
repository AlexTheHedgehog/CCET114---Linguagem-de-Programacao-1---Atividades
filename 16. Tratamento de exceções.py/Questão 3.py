import sys
# Crie um programa que solicite ao usuário uma lista de valores inteiros separados por vírgulas. Divida a
# String em valores individuais, convertendo cada String em um número inteiro. Você deve usar uma
# instrução try/except para informar ao usuário quando os valores inseridos não podem ser convertidos.

valores = input('Entre com uma lista de números inteiros, separados por vírgula: ')
inteiros = []
for i in valores:
    try:
        inteiros.append(int(i))
    except ValueError:
        pass
    except:
        print(f'O erro foi {sys.exc_info()[0]}')

print(inteiros)