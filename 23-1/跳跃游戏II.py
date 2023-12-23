class Solution:
    def jump(self, nums) -> int:

        i = 0
        n = len(nums)
        c = nums[0]
        if len(nums)==1:
            return 0
        res=1
        while i<=c:
            if i==c and c<:

            if i+nums[i] >c:
                c = i + nums[i]
            if c>=n-1:
                return res
            i+=1

a = Solution()
print(a.jump([2,3,0,1,4]))