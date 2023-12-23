import sys
def getgbs(a,b):
    x=max(a,b)
    y=min(a,b)
    z = x
    while True :
        if z%y:
            z+=x
        else:
            return z


def fan():
    chars = [i.strip() for i in sys.stdin.readlines()]
    for i in chars:
        print(i[::-1])

def val():
    nums = list(map(int, sys.stdin.readlines()))
    count=sum=count2 = 0
    for num in nums:
        if num < 0:
            count += 1
        else:
            sum += num
            count2 += 1
    print(count)
    print('%.1f'%(sum/count2))
def strcut():
    chars = [input().strip()    for i in range(int(input()))]
    for i in chars:
        num = len(i)//8
        mo = len(i)%8
        if num == 0 and mo == 0:
            continue
        x = 0
        for j in range(num):
            print(i[x:x+8])
            x+=8
        if mo != 0:
            print(i[x:].ljust(8,'0'))

def red():
    n = int(input())
    nums = list(map(int, input().strip().split()))
    count = 0
    for i in range(len(nums)):
        list1 = nums[i:]

        list1 = sorted(list(set(list1)))
        print(list1)
        count=max(count,len(list1[0:list1.index(nums[i])+1]))
    print(count)

if __name__ == "__main__":
    # nums =[i.strip().split() for i in sys.stdin.readlines()]
    # print(nums)
    # for a,b in nums:
    #     print(getgbs(int(a), int(b)))


    # nums = list(map(int,sys.stdin.readlines()))
    # print(nums)

    # val()

    # strcut()
    red()