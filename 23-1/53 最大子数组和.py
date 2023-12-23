# class Solution:
#     def maxSubArray(self, nums) -> int:
#         res = float("-INF")
#
#         for i in range(1,len(nums)+1):
#             j = 0
#             while j+i <=len(nums):
#                 # print(nums[j:j+i])
#                 res = max(res,sum(nums[j:j+i]))
#                 j+=1
#         return res

class Solution:
    def maxSubArray(self, nums) -> int:
        res = max(nums)
        count = 0
        for i in range(len(nums)):
            if count+nums[i]<0:
                count=0
            else:
                count+=nums[i]
                res = max(res,count)
        return res

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([5,4,-1,7,8]))