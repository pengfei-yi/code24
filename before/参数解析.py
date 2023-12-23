import sys
import re
for line in sys.stdin:
    s = line
    has_ = re.findall('\".*?\"',s)
    for old_s in has_:
        new_s = old_s.replace(" ","##")
        s = s.relace(old_s,new_s[1:-1])
    res = s.split()
    print(len(res))
    for c in res:
        print(c.replace("##"," "))
