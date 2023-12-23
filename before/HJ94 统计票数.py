try:
    while True:
        n = int(input())
        names = input().split()
        m = int(input())
        pick = input().split()
        res = {}
        for name in names:
            res[name] = 0
        res["Invalid"] = 0
        for p in pick:
            if res.get(p) is None:
                res["Invalid"]+=1
            else:
                res[p]+=1
        for name in names:
            print(f"{name} : {res[name]}")
        print(f"Invalid : {res['Invalid']}")


except:
    pass