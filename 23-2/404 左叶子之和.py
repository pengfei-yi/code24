class Solution:
    def __init__(self):
        self.res = 0
    def sumOfLeftLeaves(self, root) -> int:
        def dfs(root):
            if root is None:
                return
            if root.left:
                if root.left.left is None and root.left.right is None:
                    self.res+=root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res