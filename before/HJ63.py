
try:
    while True:
        s = input()
        n = int(input())

        l=0
        r = n
        res = 0
        s1 = ''
        while r<= len(s):
            tmp = 0
            tmp+= s.count("C",l,r)
            tmp+= s.count("G",l,r)
            freq = tmp/n
            # print(freq)
            if freq == 1:
                print(s[l:r])
                break
            if freq >res:
                res = freq
                s1 = s[l:r]
            l+=1
            r=l+n
        else:
            print(s1)

except:
    pass