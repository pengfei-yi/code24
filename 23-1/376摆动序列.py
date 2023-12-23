class Solution:
    def wiggleMaxLength(self, nums) -> int:
        pre = nums[0]
        cmd = ""
        count = 0
        for i in range(1,len(nums)):
            if nums[i]>pre:
                if cmd !="+":
                    cmd="+"
                else:
                    count+=1
            elif nums[i]<pre:
                if cmd !="-":
                    cmd="-"
                else:
                    count+=1
            else:
                count+=1
                cmd = ""
            pre = nums[i]
        return len(nums)-count





a = Solution()
print(a.wiggleMaxLength([1,7,4,9,2,5]))
print(a.wiggleMaxLength( [1,17,5,10,13,15,10,5,16,8]))
print(a.wiggleMaxLength( [1,2,3,4,5,6,7,8,9]))



























# class Solution:
#     def wiggleMaxLength(self, nums) -> int:
#         pre = nums[0]
#         pre_c = ""
#         res=0
#         for i in range(1,len(nums)):
#             # print(pre,nums[i])
#             if nums[i]> pre:
#                 if pre_c != "+":
#                     pre_c = "+"
#                 else:
#                     # print(nums[i])
#                     res+=1
#             elif nums[i]< pre:
#                 if pre_c != "-":
#                     pre_c = "-"
#                 else:
#                     # print(nums[i])
#                     res+=1
#             else:
#                 # print(nums[i])
#                 res+=1
#             pre = nums[i]
#
#         return len(nums)-res
