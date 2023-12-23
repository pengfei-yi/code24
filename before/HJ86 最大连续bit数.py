import sys

for line in sys.stdin:
    a = bin(int(line.strip()))
    l,r=0,0
    res = 0
    a = a[2:]+"0"
    while r<len(a):
        if a[r] == "1":
            r+=1
        else:
            res = max(res,r-l)
            r+=1
            l=r
    print(res)
