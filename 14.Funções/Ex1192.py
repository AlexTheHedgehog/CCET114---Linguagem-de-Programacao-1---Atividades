def calculo(seq):
    if seq[0] == seq[2]:
        cal = int(seq[0]) * int(seq[2])
    else:
        if seq[1].isupper():
            cal = int(seq[2]) - int(seq[0])
        if seq[1].islower():
            cal = int(seq[0]) + int(seq[2])
    
    return cal

n = int(input())

for i in range(n):
    cal = 0
    num = input()
    
    print(calculo(num))