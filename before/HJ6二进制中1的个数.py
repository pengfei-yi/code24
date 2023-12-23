import sys
for line in sys.stdin:
    a = int(line.strip())
    res = 0
    while a:
        a,m = divmod(a,2)
        if m == 1:
            res+=1
    print(res)