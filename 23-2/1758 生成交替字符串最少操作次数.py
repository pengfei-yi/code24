class Solution:
    def minOperations(self, s: str) -> int:
        cmp = ''
        a=b=0
        for i in range(len(s)+1):
            cmp+= str(i%2)
        for i in range(len(s)):
            if s[i]!=cmp[i]:
                a+=1
            if s[i]!=cmp[i+1]:
                b+=1
        return min(a,b)


a = Solution()

print(a.minOperations("0100"))