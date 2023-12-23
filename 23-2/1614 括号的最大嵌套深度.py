class Solution:
    def __init__(self):
        self.res = 0

    def maxDepth(self, s: str) -> int:
        self.func(s, 0, 0)
        return self.res

    def func(self, s, l, deep):
        self.res = max(self.res, deep)
        while l < len(s):
            if s[l] == "(":
                l = self.func(s, l + 1, deep + 1)
            elif s[l] == ")":
                return l + 1
            else:
                l+=1
