casos = int(input())
i = 1
resp = ''

while i <= casos:
    a, b, c = map(float, input().split())
    media = (a*2 + b*3 + c*5) / 10
    resp += f'{media:.1f}'

    if i < casos:
        resp += '\n'
    
    i += 1

print(resp)