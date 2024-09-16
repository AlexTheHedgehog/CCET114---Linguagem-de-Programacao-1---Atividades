while True:
    try:
        cont1 = cont2 = 0
        equacao = list(input())
        for j in equacao:
            if j == '(':
                cont1 += 1
            if j == ')':
                cont2 += 1
                if cont1 < cont2:
                    break
    
    
        if cont1 != cont2:
            print('incorrect')
        else:
            print('correct')
    except EOFError:
        break