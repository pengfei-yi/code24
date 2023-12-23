import time


def func():
    s = "wangximing"
    n = len(s)//6
    m = len(s)%6
    nums = [0 for _ in range(6)]
    for i in range(n):
        for j in range(6):
            nums[j] = nums[j] + ord(s[j+6*i])
    for k in range(m):
        nums[k] = nums[k] +ord(s[n*6+k])

    for num in nums:
        print(get_num(num),end="")

def get_num(num):
    while num >10:
        s = f"{num}"
        sum = 0
        for n in s:
            sum += int(n)
        num = sum
    return num

func()
# print(get_num(228))
