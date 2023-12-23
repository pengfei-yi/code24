class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        _next = [0]
        n = len(needle)
        for i in range(1,n):
            tmp = 0
            for j in range(0,i):
                left = needle[:j+1]
                right = needle[i-j:i+1]
                # print(left,right)
                if left == right:
                    tmp = max(tmp,j+1)
            _next.append(tmp)
        print(_next)
        j = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j+=1
                i+=1
                if j == n:
                    return i - n
            elif j >0:
                j = _next[j-1]
            else:
                i+=1

        return -1



a = Solution()

print(a.strStr("sadbutsad","sad"))
print(a.strStr("leetcode","leeto"))
print(a.strStr("abcccabcc","bccc"))
