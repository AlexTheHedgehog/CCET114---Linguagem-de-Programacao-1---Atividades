while True:
    try:
        rec = int(input())

        if rec == 0:
            print('vai ter copa!')
        elif rec > 0:
            print('vai ter duas!')
    except EOFError:
        break