n1, n2, n3, n4 = map(float, input().split())

media = (n1*2 + n2*3 + n3*4 + n4) / 10

print(f'Media: {media:.1f}')

if media > 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota = float(input('Nota do exame: '))
    media_final = (media + nota) / 2

    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    
    print(f'Media final: {media_final}')