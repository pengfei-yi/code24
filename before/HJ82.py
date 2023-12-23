try:
    while True:
        n,m = map(int,input().split("/"))
        res = [f"1/{m}"for i in range(n)]
        print("+".join(res))
except:
    pass
