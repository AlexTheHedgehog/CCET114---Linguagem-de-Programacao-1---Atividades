a, b, c = map(float, input().split())

if a + b > c and b + c > a and a + c > b:
    print(f'Perimetro = {a+b+c}')
else:
    print(f'Area = {((a+b)*c)/2}')