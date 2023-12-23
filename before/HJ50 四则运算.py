s = input()

def func(i,s):
    pre = "+"
    res = []

    while i <(len(s)):

        c = s[i]
        if c.isdigit():
            j = i +1
            while j< len(s) and s[j].isdigit():
                c+=s[j]
                j+=1
            i = j-1
            c = int(c)
            if pre == "+":
                res.append(c)
            elif pre =="-":
                res.append(-c)
            elif pre == "*":
                res.append(res.pop()*c)
            else:
                res.append(res.pop()//c)
            pre = "+"
        elif c in "-/*":
            pre = c
        elif c in "([{":
            i,ret = func(i+1,s)
            if pre == "+":
                res.append(ret)
            elif pre == "-":
                res.append(-ret)
            elif pre == "*":
                res.append(res.pop() * ret)
            else:
                res.append(res.pop() // ret)
            pre = "+"
        elif c in ")]}":
            # print(res)
            return i,sum(res)
        i+=1
    # print("res",res)
    return i,sum(res)
print(func(0,s)[1])