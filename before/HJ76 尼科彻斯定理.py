import sys

for line in sys.stdin:
    a = int(line.strip())
    b = a**3
    # print(b)
    c = a*(a-1)
    res = (b-c)//a
    print(res,end="")
    for j in range(1,a):
        print(f"+{res+j*2}",end='')

