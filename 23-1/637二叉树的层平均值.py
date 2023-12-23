class Solution:
    # def __init__(self):
    #     self.res = []
    def averageOfLevels(self, root):
        queue = [root]
        res =[]
        while queue:
            sums = 0
            c=len(queue)
            for i in range(c):
                cur = queue.pop(0)
                sums+=cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(sums/c)
        return res


