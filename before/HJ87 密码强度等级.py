import sys
import re


def lenth(s):
    if len(s)<=4:
        return 5
    return 25 if len(s)>=8 else 10

def alpha(s):
    res = 0
    if re.findall("[A-Z]",s):
        res+=10
    if re.findall("[a-z]",s):
        res+=10
    return res

def numbers(s):
    res = 0
    tmp = len(re.findall("[0-9]",s))
    if tmp:
        res+=10
    if tmp>1:
        res+=10
    return res
def fuhao(s):
    res = 0
    n = len(s)
    n1 = len(re.findall("[0-9a-zA-Z]",s))
    tmp = n-n1
    if tmp:
        res+=10
    if tmp>1:
        res+=15
    return res



for line in sys.stdin:
    a = line.strip()
    b = lenth(a)
    c = alpha(a)
    d = numbers(a)
    e = fuhao(a)
    # print(b,c,d,e)
    res = b+c+d+e
    if d:
        if c==20 and e :
            # print("ww")
            res+=5
        elif c and e :
            # print("ss")
            res+=3
        elif c:
            # print("aa")
            res+=2
    if res>=90:print("VERY_SECURE")
    elif res>=80:print("SECURE")
    elif res>=70:print("VERY_STRONG")
    elif res>=60:print("STRONG")
    elif res>=50:print("AVERAGE")
    elif res>=25:print("WEAK")
    else:
        print("VERY_WEAK")




