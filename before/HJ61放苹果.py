try:
    while True:
        m,n = map(int,input().split())
        res = []
        def backtrack(choose,path):
            if len(path) == n:
                if sum(path) == m:
                    res.append(path.copy())
                return

            for i in range(len(choose)):
                path.append(choose[i])
                if sum(path)<=m:
                    backtrack(choose[i+1:],path)
                path.pop()
        choose = list(range(m+1))
        backtrack(choose,[])

except:
    pass