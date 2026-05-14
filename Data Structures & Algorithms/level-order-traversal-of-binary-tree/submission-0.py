# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque()
        res =[]
        dq.append(root)
        while dq:
            l = len(dq)
            level = []
            for i in range(l):
                current = dq.popleft()
                level.append(current.val)
                if current.left:
                    dq.append(current.left)
                if current.right:
                    dq.append(current.right)
            res.append(level[:])
        return res
                


        
            
            
            