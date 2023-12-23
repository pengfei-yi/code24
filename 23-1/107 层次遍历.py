# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def levelOrderBottom(self, root):
        def dfs(root,deep):
            if not root:
                return
            if len(self.res)<deep:
                self.res.append([])
            self.res[deep-1].append(root.val)
            dfs(root.left,deep+1)
            dfs(root.right,deep+1)
        dfs(root,1)
        return self.res[::-1]