try:

    def func(x):

        return
    while True:
        n = int(input())
        tran = list(map(int,input().split()))
        tran.reverse()
        res = []
        def backtrack(t,choose,path):
            if len(path) == n:
                res.append(path[:])
            # print("choose",choose)
            # print("path",path)
            for cmd in ("push","pop"):
                if cmd == "pop":
                    if not choose:
                        continue
                    path.append(choose.pop())
                    backtrack(t,choose,path)
                    choose.append(path.pop())

                else:
                    if not t:
                        continue
                    choose.append(t.pop())
                    backtrack(t,choose,path)
                    t.append(choose.pop())
        backtrack(tran,[],[])
        print(res)
        for line in sorted(res):
            print(" ".join(map(str,line)))


except:
    pass