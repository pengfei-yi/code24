class Solution:
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while queue:
            tmp =[]
            for i in range(len(queue)):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp)
        return res
