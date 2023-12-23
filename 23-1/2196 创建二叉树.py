# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions):
        self.dict_ = dict()
        dumy = set()
        for p,c,l in descriptions:
            dumy.add(p)
            if self.dict_.get(p) is None:
                self.dict_[p] = {l:c}
            else:
                self.dict_[p][l] = c
        for i in range(len(descriptions)):
            dumy-={descriptions[i][1]}

        print(dumy)
        print(self.dict_)
        root = TreeNode(dumy.pop())
        self.inittree(root)
        return root


    def inittree(self,root):
        node = self.dict_.get(root.val)
        if node is None:
            return
        left = self.dict_[root.val].get(1)
        right = self.dict_[root.val].get(0)
        if left is not None:
            root.left = TreeNode(left)
            self.inittree(root.left)
        if right is not None:
            root.right = TreeNode(right)
            self.inittree(root.right)



a = Solution()
a.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])