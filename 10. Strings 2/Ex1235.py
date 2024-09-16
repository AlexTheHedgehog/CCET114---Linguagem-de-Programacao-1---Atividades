n = int(input())

for i in range(n):
    msg = input()
    metade = int(len(msg) / 2)
    msg1 = msg[:metade]
    msg2 = msg[metade:]

    resp = msg1[::-1] + msg2[::-1]
    print(resp)