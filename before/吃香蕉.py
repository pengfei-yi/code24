import math
class Solution:
    def minEatingSpeed(self, piles, H):
        minSpeed = 1
        maxSpeed = max(piles)
        while minSpeed<maxSpeed:
            mid =(minSpeed + maxSpeed)>>1
            if self.Eating(piles,mid) <H:
                minSpeed = mid+1
            else:
                maxSpeed=mid
        return minSpeed

    def Eating(self,piles,speed):
        eatime = 0
        for pile in piles:
            eatime+=math.ceil(pile/speed)
        return eatime
s =Solution()
piles = [3,6,7,11]
H = 8
# piles= [30, 11, 23, 4, 20]
# H=5
print(s.minEatingSpeed(piles,H))