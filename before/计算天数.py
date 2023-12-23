try:
    while True:
        y, m, d = map(int, input().split())
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y % 4 == 0 and y % 100 != 0 :
            days[2] = 29
        for i in range(1, m):
            d += days[i]
        print(d)


except:
    pass
