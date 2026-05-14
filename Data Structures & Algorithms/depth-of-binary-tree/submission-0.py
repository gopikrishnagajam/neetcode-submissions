# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m=0
        def dfs(node ,count):
            nonlocal m
            if not node:
                m = max(m,count)
                return
            dfs(node.left , count+1)
            dfs(node.right, count+1)
            return
        dfs(root, 0)
        return m