def func(needle):
    _next = [0]
    n = len(needle)
    for i in range(1, n):
        tmp = 0
        for j in range(0, i):
            left = needle[:j + 1]
            right = needle[i - j:i + 1]
            # print(left,right)
            if left == right:
                tmp = max(tmp, j + 1)
        _next.append(tmp)
    return _next

def getNext( nxt, s):
    nxt[0] = 0
    j = 0
    print(s)
    for i in range(1, len(s)):
        print(i,s[i],"--",j,s[j])
        while j > 0 and s[i] != s[j]:
            print(i,s[i],"---",j,s[j])
            j = nxt[j - 1]

        if s[i] == s[j]:
            j += 1
        nxt[i] = j
    return nxt
s = "adcdadcdff"
print(func(s))

print(getNext([0]*len(s),s))