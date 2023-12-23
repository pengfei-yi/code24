import sys

for line in sys.stdin:
    a = int(line)
    res= 0
    for i in range(1,a+1):
        sums = 0
        # tmp = f"{i}:"
        for j in range(1,i//2+1):
            if i%j==0:
                sums+=j
                # tmp += f" {j}"
                if sums >i:
                    break
        else:
            if sums == i:
                res+=1
        # print(tmp)
    print(res)