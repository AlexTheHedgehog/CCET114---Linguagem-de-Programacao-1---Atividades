n = int(input())
resp = ''
i = 1
while i <= n:
    num = int(input())
    if num != 0:
        if num % 2 == 0:
            resp += 'EVEN'
        else:
            resp += 'ODD'

        if num > 0:
            resp += ' POSITIVE'
        elif num < 0:
            resp += ' NEGATIVE'
    else:
        resp += 'NULL'
    
    if i < n:
        resp += '\n'
    i += 1

print(resp)