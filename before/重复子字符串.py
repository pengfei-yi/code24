class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        next = self.getNext(s)
        if next[-1] !=0 and len(s)%(len(s)-next[-1]) == 0:
            return True
        return False

    def getNext(self,s):
        res = [0]*len(s)
        j= 0
        for i in range(1,len(s)):
            while j>0 and s[i] !=s[j]:
                j = res[j-1]
            if s[i] == s[j]:
                j+=1
            res[i] = j
        return res
