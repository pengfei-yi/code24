class Solution:
    def maxDistance(self, grid) -> int:
        n = len(grid)
        def func(x,y):
            ret = []
            for k,l in [[1,0],[-1,0],[0,1],[0,-1]]:
                if 0<=x+k<n and 0<=y+l<n and grid[x+k][y+l]==0:
                    grid[x+k][y+l]=1
                    ret.append([x+k,y+l])
            # print(ret)
            return ret
        res = 0
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i,j])
        if not queue or len(queue)==n*n:
            return -1
        while queue:
            for i in range(len(queue)):
                tmp = queue.pop(0)
                queue.extend(func(*tmp))
            print(queue)
            if queue:
                res+=1
        return res


a = Solution()
print(a.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))