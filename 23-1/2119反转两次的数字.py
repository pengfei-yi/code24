class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        tmp = int(str(num)[::-1])
        tmp = int(str(tmp)[::-1])
        return num==tmp