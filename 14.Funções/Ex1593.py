def count_bin_1(decimal:int):
    cont = 0
    binario = str(bin(decimal))
    
    for i in binario[2:]:
        if i == '1':
            cont += 1
    
    return cont

t = int(input())

for i in range(t):
    num = int(input())
    print(count_bin_1(num))