# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        dq = deque()
        dq.append(root)
        while dq:
            current =dq.popleft()
            if current.left:
                dq.append(current.left)
            temp = current.left
            current.left = current.right
            if current.right:
                dq.append(current.right)
            current.right = temp
        return root
                