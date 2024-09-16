n = int(input())

for i in range(n):
    car = input()
    num1 = int(car[2:4])
    num2 = int(car[5:8])
    num3 = int(car[11:13])
    soma = num1 + num2 + num3
    print(soma)