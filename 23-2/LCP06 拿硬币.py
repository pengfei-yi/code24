import math


class Solution:
    def minCount(self, coins) -> int:
        res = 0
        for i in range(len(coins)):
            res+= math.ceil(coins[i]/2)
        return res
