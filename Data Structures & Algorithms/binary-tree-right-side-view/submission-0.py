# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        d =deque()
        res =[]
        d.append(root)
        while d:
            l = len(d)
            level =[]
            for i in range(l):
                c = d.popleft()
                level.append(c.val)
                if c.left:
                    d.append(c.left)
                if c.right:
                    d.append(c.right)
            res.append(level[-1])
        return res
        