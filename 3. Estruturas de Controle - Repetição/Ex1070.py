x = int(input())
impar = 0
while impar < 6:
    if x % 2 != 0:
        print(x)
        impar += 1
    
    x += 1