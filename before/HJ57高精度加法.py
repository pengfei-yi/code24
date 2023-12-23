import sys
data = sys.stdin.readlines()
for i in range(0,len(data),2):
    a = data[i].strip()
    b = data[i+1].strip()
    lenth = max(len(a),len(b))
    a = a.rjust(lenth,"0")
    b = b.rjust(lenth,"0")
    res = ''
    tmp = 0
    for j in range(lenth-1,-1,-1):
        sums = int(a[j])+int(b[j])+tmp
        tmp,cur =divmod(sums,10)
        res = str(cur) + res
    if tmp:
        res = str(tmp) + res
    print(res)