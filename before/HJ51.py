import sys

class Node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

data = sys.stdin.readlines()
for i in range(0,len(data),3):
    n = int(data[i].strip())
    values = list(map(int,data[i+1].strip().split()))
    k = int(data[i+2].strip())

    head = Node()
    p = head
    for t in values:
        p.next = Node(t)
        p = p.next

    p = head
    q = head
    for i in range(k):
        p = p.next
    while p:
        p = p.next
        q = q.next
    print(q.val)




