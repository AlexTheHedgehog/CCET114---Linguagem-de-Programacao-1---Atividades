# Crie uma função que recebe um String como parâmetro e verifica se a mesma é composta apenas por
# caracteres maiúsculos. A função deve lançar dois tipos de exceções: uma para indicar se existe algum
# caractere que não é uma letra e a outra para indicar se algum dos caracteres não é maiúsculo.
class NaoLetraError(Exception):
    pass

class NaoMaiusError(Exception):
    pass

def chars_upper(parametro):
    try:
        for i in parametro:
            if i.isalpha() == False:
                raise NaoLetraError('Um ou mais caracteres não são uma letra!')
            elif i.islower():
                raise NaoMaiusError('Um ou mais caracteres não estão em maiúsculo!')
    except NaoLetraError as nle:
        print(f'ERRO: {nle}\nEntrada: {parametro}')
    except NaoMaiusError as nme:
        print(f'ERRO: {nme}\nEntrada: {parametro}')

entrada = input('Entre com uma palavra ou frase: ')
chars_upper(entrada)