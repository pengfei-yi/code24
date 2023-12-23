import sys
from math import sqrt

chi = [2,3,5]
for i in range(6,1000):
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            break
    else:
        chi.append(i)
# print(chi)

for line in sys.stdin:
    a = int(line.strip())
    idx = 0
    res = [0,0]
    _min = 1000
    while chi[idx]<= a//2:
        if a-chi[idx] in chi:
            if a-chi[idx]-chi[idx] <_min:
                res[0]=chi[idx]
                res[1]=a-chi[idx]
        idx+=1
    for k in res:
        print(k)



