import re

try:
    while True:
        s = input()
        res = re.findall("\d+",s)
        res.sort(key=lambda x:-len(x))
        n = len(res[0])
        res = list(filter(lambda x:len(x)==n,res))
        print(f"{''.join(res)},{len(res[0])}")




except:
    pass