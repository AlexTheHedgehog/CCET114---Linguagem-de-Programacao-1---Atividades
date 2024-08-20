n = int(input())
m = int(input())
fig = []

for i in range(m):
    x = int(input())
    if x not in fig:
        fig.append(x)
    
falta = n - len(fig)
print(falta)