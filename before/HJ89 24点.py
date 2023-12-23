ruler = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
try:
    while True:
        s = input()
        if "JOKER" in s.upper():
            print("ERROR")
            continue
        s= s.split()
        res = []
        def backtrack(choose,path,sums):
            # print(sums)
            if len(path) == 4:
                if sums == 24:
                    res.append(path.copy())
                return
            for i in range(len(choose)):
                for cmd in ("+","-","*","//"):
                    if len(path) == 0:
                        if cmd == "+":
                            path.append(f"{choose[i]}")
                            backtrack(choose[:i]+choose[i+1:],path,ruler.index(choose[i]))
                            path.pop()
                    else:
                        path.append(f"{cmd}{choose[i]}")
                        backtrack(choose[:i]+choose[i+1:],path,eval(f"{sums}{cmd}{ruler.index(choose[i])}"))
                        path.pop()
        backtrack(s,[],0)
        # print(res)
        if res:
            tmp = "".join(res[0])
            print(tmp.replace("//","/"))
        else:
            print("NONE")

except:
    pass
# sums=16
# cmd = "*"
# sums = eval(f"{sums}{cmd}{ruler.index('Q')}")
# print(sums)