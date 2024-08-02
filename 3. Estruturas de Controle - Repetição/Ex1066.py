par = impar = positivo = negativo = 0

for i in range(0, 5):
    num = int(input())

    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1

print(f'''{par} valor(es) par(es)
{impar} valor(es) impar(es)
{positivo} valor(es) positivo(s)
{negativo} valor(es) negativo(s)''')