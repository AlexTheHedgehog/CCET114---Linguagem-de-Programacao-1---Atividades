# Crie uma exceção chamada FahrenheitError. Desenvolva uma função para converter temperaturas em
# graus Fahrenheit para graus Celsius, ambas representadas em ponto flutuante (float). Porém, caso o valor a
# ser convertido seja menor que zero absoluto (-459,67°F) deve-se lançar a exceção FahrenheitError. A
# fórmula para conversão é dada por: C = 5 (F − 32) / 9

class FarenheitError(Exception):
    pass

def convert(f:float):
    try:
        if f < -459.67:
            raise FarenheitError('Menor que zero absoluto!')
        c = 5 * (f - 32) / 9
        print(f'{f:.2f}°F = {c:.2f}°C')
    except FarenheitError as frr:
        print(f'ERRO: {frr}\nEntrada: {f}°F')

entrada = float(input('Entre com uma temperatura em Farenheit: '))
convert(entrada)