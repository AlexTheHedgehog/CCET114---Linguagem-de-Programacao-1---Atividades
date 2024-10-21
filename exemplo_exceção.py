while True:
    try:
        entrada = input("Entre com um número: ")
        x = 5 / int(entrada)
        print(x)
    except ValueError as erro:
        print(str(erro))
        print(f'Tente novamente...')
    except ZeroDivisionError:
        print('Não é possível dividir por zero.\nTente novamente...')
    except EOFError as eor:
        print('Fim do programa.')
        break
    finally:
        print(f'A entrada foi {entrada}')