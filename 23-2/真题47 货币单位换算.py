
import re

def func():
    map_ = {"CNY":100,"JPY":10000/1825,"HKD":10000/123,"EUR":10000/14,"GBP":10000/12,
            "fen":1,"sen":100/1825,"cents":100/123,
            "eurocents":100/14,"pence":100/12}

    n = int(input())
    ret = 0

    for i in range(n):
        line = input()
        bi =list(re.findall("[A-Z a-z]+",line))
        # print(bi)
        nums = list(re.findall("\d+",line))
        # print(nums)
        cur=0
        for j in range(len(bi)):
            cur= cur + map_[bi[j]]* int(nums[j])

        ret+=cur
    print(int(ret))

func()