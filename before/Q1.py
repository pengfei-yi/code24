def get_area(comlist, e):
    area = 0
    y = comlist[0][1]
    for i in range(1, len(comlist)):
        area += (comlist[i][0] - comlist[i - 1][0]) * abs(y)
        y += comlist[i][1]
    if comlist[-1][0] < e:
        area += (e - comlist[-1][0]) * abs(y)
    return area


if __name__ == '__main__':
    # comm,e = map(int,input().strip().split())
    # comlist= []
    # for i in range(comm):
    #     comlist.append([int(v) for v in input('请输入以空格分隔的整数').strip().split()])
    e = 10
    comlist = [[1,1],[2,1],[3,1],[4,-2]]
    # e = 4
    # comlist = [[0, 1], [2, -2]]
    print(get_area(comlist, e))
