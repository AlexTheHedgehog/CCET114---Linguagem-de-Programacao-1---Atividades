n = int(input())

for i in range(n):
    msg = list(input().split())
    msg2 = []

    for j in range(len(msg)):
        palavra = list(msg[j])
        if len(msg[j]) >= 10 and msg[j][1:9] == 'oulupukk':
            if msg[j][0] != 'J':
                palavra[0] = 'J'

            if msg[j][9] != 'i':
                palavra[9] = 'i'
        
        palavra = ''.join(palavra)
        
        msg2.append(palavra)

    print(' '.join(msg2))