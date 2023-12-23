_input = list(map(int,input().split()))
n = _input.pop(0)
li = [_input.pop(0)]
_del = _input.pop()
for i in range(0,len(_input),2):
    l = _input[i]
    r = _input[i+1]
    idx = li.index(r)
    li.insert(idx+1,l)
li.remove(_del)
for t in li:
    print(t,end=" ")


