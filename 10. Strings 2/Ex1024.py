n = int(input())
#ascii_1 = list(map(chr, range(97, 123)))
#ascii_2 = list(map(chr, range(65, 91)))

for i in range(n):
    resp1 = resp2 = ''
    msg = input()

    for j in msg:
#        if j in ascii_1 or j in ascii_2:
        if j.isalpha():
            ordem = int(ord(j))
            letra = chr(ordem + 3)
        else:
            letra = j
        resp1 += letra
    resp1 = resp1[::-1]
    
    for j in range(len(resp1)):
        letra = resp1[j]
        if j >= len(resp1)//2:
            ordem = int(ord(resp1[j]))
            letra = chr(ordem - 1)
        resp2 += letra
    
    print(resp2)