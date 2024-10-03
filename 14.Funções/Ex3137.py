def digitos(num):
    return len(str(num))

p = int(input())
cont = 0

for i in range(1, p+1):
    cont += digitos(i)

print(cont)