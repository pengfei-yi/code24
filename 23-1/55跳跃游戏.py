class Solution:
    def canJump(self, nums) -> bool:
        i = 0
        n = len(nums)
        c = nums[0]
        while i<=c:
            c = max(i+nums[i],c)
            if c>=n-1:
                return True
            i+=1
        return False


a = Solution()
print(a.canJump( [2,3,1,1,4]))
print(a.canJump( [3,2,1,0,4]))
print(a.canJump( [1]))
print(a.canJump( [1,2]))
print(a.canJump( [2,0,1,1,2,1,0,0,0]))
print(a.canJump( [5,9,3,2,1,0,2,3,3,1,0,0]))