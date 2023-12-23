try:
    while True:
        s = input()
        t = input()
        if len(s) > len(t):
            s,t = t,s
        for c in s:
            if t.find(c) == -1:
                print("false")
                break
        else:
            print("true")
except:
    pass