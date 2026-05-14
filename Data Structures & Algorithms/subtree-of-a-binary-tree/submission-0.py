# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            if not p and not q:
                return True
            elif (not p and q) or (not q and p):
                return False
            elif p.val != q.val:
                return False
            else:
                return sameTree(p.left, q.left) and sameTree(p.right ,q.right)
        dq = deque()
        dq.append(root)
        while dq:
            current = dq.popleft()
            if sameTree(current , subRoot):
                return True
            if current.left:
                dq.append(current.left)
            if current.right:
                dq.append(current.right)
        return False