class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        res = []
        k = 0
        while k<=len(nums)-3:
            if k>0 and nums[k] == nums[k-1]:
                k+=1
                continue
            l = k+1
            l1 =l
            r = len(nums)-1
            r1 =r
            while l<r:
                if l>l1 and nums[l]==nums[l-1]:
                    l+=1
                    continue
                if r<r1 and nums[r]==nums[r+1]:
                    r-=1
                    continue
                if nums[k]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[k]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    print(k,l,r)
                    res.append([nums[k],nums[l],nums[r]])
                    l+=1
                    r-=1
            k+=1
        return res



a = Solution()

print(a.threeSum([-1,0,1,2,-1,-4]))