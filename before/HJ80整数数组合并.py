try:
    while True:
        n = int(input())
        n1 = list(map(int, input().split()))
        m = int(input())
        m1 = list(map(int, input().split()))
        # res = []
        # while n1 and m1:
        #     if n1[0]<m1[0]:
        #         tmp = n1.pop(0)
        #     else:
        #         tmp = m1.pop(0)
        #     if res and res[-1]>= tmp:
        #         continue
        #     res.append(tmp)
        # while n1:
        #     if n1[0] > res[-1]:
        #         res.append(n1.pop(0))
        # while m1:
        #     if m1[0] > res[-1]:
        #         res.append(m1.pop(0))
        # for i in res:
        #     print(i,end="")
        n1.extend(m1)
        n1 = list(set(n1))
        n1.sort()
        for i in n1:
            print(i,end="")


except:
    pass
