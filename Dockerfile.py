from random import random
N = 5
a = []
for i in range(N):
    z = []
    for j in range(N):
        n = int(random() * 100) - 50
        z.append(n)
        print("%4d" % n, end='')
    print()
    a.append(z)
print()
 
for i in range(N):
    if a[i][i] > 0:
        print("%4d" % a[i][i], end='')
print()