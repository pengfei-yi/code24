try:
    while True:
        n = int(input())
        cmd = input()

        songs = [i for i in range(1,n+1)]
        seek = 0

        def pageU(l,seek):
            if seek == 0:
                if l>1:
                    l-=4
                    if l<1:
                        l=1
                else:
                    l=n-3
            else:
                seek-=1
            return l,seek

        def pageD(l,seek):
            if seek == 3:
                if l>1:
                    l-=4
                    if l<1:
                        l=1
                else:
                    l=n-3
            else:
                seek+=1
            return l,seek


except:
    pass