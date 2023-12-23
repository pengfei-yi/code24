import sys

for line in sys.stdin:


    def func(i,s):
        res = []
        pre = "+"
        while i< len(s):
            c = s[i]
            # print("c:",c)
            if c.isdigit():
                while i+1<len(s) and s[i+1].isdigit():
                    c+= s[i+1]
                    i+=1
                c=int(c)
                if pre =="+":
                    res.append(c)
                elif pre == "-":
                    res.append(-c)
                elif pre == "*":
                    res.append(res.pop()*c)
                else:
                    res.append(res.pop()//c)
                pre = "+"
            elif c in "+-*/":
                pre = c
            elif c =="(":
                i,c = func(i+1,s)
                if pre =="+":
                    res.append(c)
                elif pre == "-":
                    res.append(-c)
                elif pre == "*":
                    res.append(res.pop()*c)
                else:
                    res.append(res.pop()//c)
            else:
                # print(res)
                return i,sum(res)
            i+=1

        return i,sum(res)

    print(func(0,str(line))[1])