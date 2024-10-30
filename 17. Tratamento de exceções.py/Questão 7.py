import sys
# Crie um programa que solicitará uma confirmação: sim ou não, que deverá ser impressa. Considere que
# os usuários podem inserir quaisquer valores, você precisa garantir que as diferentes possibilidades sejam
# tratadas corretamente. Se uma resposta desconhecida for fornecida, o programa deve gerar uma exceção
# personalizada chamada RespostaInvalidaError e forçar que o usuário forneça um valor válido.
class RespostaInvalidaError(Exception):
    pass

while True:
    try:
        resp = input('Você acha minhas habilidades de programação boas? [sim/não]: ')
        if resp not in ['sim', 'não']:
            raise RespostaInvalidaError('Valor inválido!')
        break
    except RespostaInvalidaError as rie:
        print(f'ERRO: {rie}\nPor favor, forneça um valor válido.')
    except:
        print(f'ERRO: {sys.exc_info()[0]}')