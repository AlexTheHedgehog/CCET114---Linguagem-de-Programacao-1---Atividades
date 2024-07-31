from math import sqrt

a, b, c = map(float, input().split())
r1 = r2 = 0
delta = b**2 - 4*a*c

if delta >= 0:
    r1 = ((-b) + sqrt(delta)) / (2*a)
    r2 = ((-b) - sqrt(delta)) / (2*a)
    print(f'R1 = {r1}\nR2 = {r2}')
elif delta < 0:
    print('Impossivel calcular')