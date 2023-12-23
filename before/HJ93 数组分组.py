try:
    while True:
        n = int(input())
        nums = list(map(int,input().split()))
        n1,n2=[],[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] % 5 ==0:
                n1.append(nums.pop(i))
            elif nums[i] % 3 ==0:
                n2.append(nums.pop(i))
        k = abs(sum(n1)-sum(n2))
        if  -sum(nums) >k:
            tmp = sum(nums)+k
        else:
            tmp = sum(nums)-k
        if tmp %2!=0:
            print("false")
            continue
        taget = tmp//2
        # print("taget:",taget)
        res = ["false"]
        def backtrack(choose,path,taget):
            if sum(path)>taget:
                return
            elif sum(path) == taget:
                # print(path)
                res[0] = "true"
                return
            for i in range(len(choose)):
                path.append(choose[i])
                backtrack(choose[:i]+choose[i+1:],path,taget)
                path.pop()
        backtrack(nums,[],taget)
        print(res[0])
except:
    pass