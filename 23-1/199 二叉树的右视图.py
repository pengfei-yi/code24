# class Solution:
#     def __init__(self):
#         self.res = []
#     def rightSideView(self, root):
#         def dfs(root,deep):
#             if not root:
#                 return
#             if len(self.res)<deep:
#                 self.res.append(0)
#             self.res[deep-1] = root.val
#             dfs(root.left,deep+1)
#             dfs(root.right,deep+1)
#         dfs(root,1)
#         return self.res
