while True:
    try:
        d, n = input().split()
        if d == n == '0':
            break
        
        v = n.replace(d, '')

        if v == '':
            v = 0
        else:
            v = int(v)
        
        print(v)
    
    except EOFError:
        break