def func():
    res = set()
    n = int(input())
    nums = []
    a = map(int,input().split())
    b = list(map(int,input().split()))
    for i,v in enumerate(a):
        nums.extend([v]*b[i])
    def backtrack(choose,path):
        res.add(path)
        for i in range(len(choose)):
            if i!=0 and choose[i] == choose[i-1]:
                continue
            backtrack(choose[i+1:],path+choose[i])
    backtrack(nums,0)
    print(len(res))


func()