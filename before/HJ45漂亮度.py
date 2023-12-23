from collections import Counter

n = int(input())
names = [input() for i in range(n)]
for name in names:
    ret = 0
    cur = 26
    res = list(Counter(name).values())
    res.sort(reverse=True)
    for j in res:
        ret += j*cur
        cur-=1
    print(ret)