class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        def backtrack(choose,path):
            res.append(path.copy())
            for i in range(len(choose)):
                if i and choose[i] == choose[i-1]:
                    continue
                backtrack(choose[i+1:],path+[choose[i]])
        backtrack(nums,[])
        return res