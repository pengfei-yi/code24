class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n>1:
            res+=n//2
            n =int(n/2+0.5)
        return res