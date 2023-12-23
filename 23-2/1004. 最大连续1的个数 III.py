class Solution:
    def longestOnes(self, nums, k: int) -> int:
        l = 0
        r = 0
        c=0
        res=0
        while r<len(nums):
            if nums[r] == 0:
                c+=1
                while c>k:
                    if nums[l] ==0:
                        c-=1
                    l+=1
            r+=1
            res = max(r-l,res)
        return res

a = Solution()
print(a.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(a.longestOnes( [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))