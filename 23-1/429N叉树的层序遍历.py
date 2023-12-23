"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.res = []
    def levelOrder(self, root):
        def dfs(root,deep):
            if not root:
                return
            if len(self.res)<deep:
                self.res.append([])
            self.res[deep-1].append(root.val)
            for i in range(len(root.children)):
                dfs(root.children[i],deep+1)
        dfs(root,1)
        return self.res
