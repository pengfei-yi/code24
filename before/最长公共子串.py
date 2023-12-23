try:
    while True:
        a = input()
        b = input()
        if len(a) <= len(b):
            a,b= b,a

        l = 0
        r = 0
        while r < len(a):
            if a[l:r+1] in  b:
                r+=1
                # print(a[l:r+1])
            else:
                l+=1
                r+=1
        # print(l,r)
        print(r-l)



except:
    pass