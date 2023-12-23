


def dfs(x,y):
    if x == m and y == n:
        res[0]+=1
        return
    for i,j in ((0,1),(1,0)):
        if x+i<=m and y+j<=n:
            dfs(x+i,y+j)

try:
    while True:
        m,n = map(int,input().split())
        grid = [[0]*(n+1) for i in range(m+1)]
        res = [0]
        dfs(0,0)
        print(res[0])



except:
    pass