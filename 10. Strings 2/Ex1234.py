while True:
    try:
        x = input()
        cont = 0
        resp = ''

        for i in x:
            if i != ' ' and cont % 2 != 0:
                resp += i.lower()
                cont += 1
            elif i != ' ' and cont % 2 == 0:
                resp += i.upper()
                cont += 1
            else:
                resp += ' '

        print(resp)
    except EOFError:
        break