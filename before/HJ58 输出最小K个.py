import  heapq

try:
    while True:
        m,n = map(int,input().split())
        nums = map(int,input().split())
        for i in heapq.nsmallest(n,nums):
            print(i,end=" ")
except:
    pass