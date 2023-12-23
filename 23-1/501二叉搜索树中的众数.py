# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.pre = None
        self.maxcount = 1
        self.curcount = 1
        self.res = []
    def findMode(self, root):
        def bl(root):
            if not root:
                return
            bl(root.left)
            if root.val == self.pre:
                self.curcount+=1
            else:
                self.curcount =1
            if self.curcount>self.maxcount:
                self.res.clear()
                self.res.append(root.val)
                self.maxcount = self.curcount
            elif self.curcount==self.maxcount:
                self.res.append(root.val)
            self.pre =root.val
            bl(root.right)
        bl(root)
        return self.res
