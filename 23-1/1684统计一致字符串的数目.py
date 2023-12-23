class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        res = 0
        allowed = set(allowed)
        for c in words:
            if not set(c)-allowed:
                res+=1
        return res


