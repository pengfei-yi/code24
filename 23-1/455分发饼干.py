class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        j = 0
        for i in range(len(s)):
            if j<len(g)and g[j]<= s[i]:
                j+=1
        return j

