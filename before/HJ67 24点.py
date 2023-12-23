import sys

for line in sys.stdin:
    a = list(map(int,line.split()))
    def dfs(a,path):
        if sum(path) == 24:
            return True
        for i in range(len(a)):
            for j in "+-*/":
                if not path and j in "*/":
                    continue
                if j=="+":
                    path.append(a[i])
                    ret = dfs(a[:i]+a[i+1:],path)
                    if ret:return True
                    path.pop()
                elif j=="-":
                    path.append(-a[i])
                    ret = dfs(a[:i]+a[i+1:],path)
                    if ret:return True
                    path.pop()
                elif j=="*":
                    pre = path.pop()
                    path.append(pre*a[i])
                    ret = dfs(a[:i]+a[i+1:],path)
                    if ret:return True
                    path.pop()
                    path.append(pre)
                elif j=="/":
                    pre = path.pop()
                    path.append(pre//a[i])
                    ret = dfs(a[:i]+a[i+1:],path)
                    if ret:return True
                    path.pop()
                    path.append(pre)
    if dfs(a,[]):
        print("true")
    else:
        print("false")