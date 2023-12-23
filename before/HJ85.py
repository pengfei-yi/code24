import sys

def check(s):
    return True if s==s[::-1] else False



def func(a):
    for i in range(len(a)):
        l = 0
        r = len(a)-i
        while r<=len(a):
            if check(a[l:r]):
                print(r-l)
                return
            l+=1
            r+=1

for line in sys.stdin:
    a = line.strip()
    func(a)


