try:
    while True:
        m,n = map(int,input().split())
        if m >9 or n>9:
            print(-1)
        else:print(0)
        x1,y1,x2,y2 = map(int,input().split())
        if 0<=x1<m and 0<=x2<m and 0<=y1<n and 0<=y2<n:
            print(0)
        else:
            print(-1)
        x = int(input())
        if 0<=x<m and m<9:
            print(0)
        else:
            print(-1)

        y = int(input())
        if 0<=y<n and n<9:
            print(0)
        else:
            print(-1)
        x,y = map(int,input().split())
        if 0<=x<m and 0<=y<n :
            print(0)
        else:
            print(-1)

except:
    pass
