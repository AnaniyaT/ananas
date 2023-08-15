# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return (0, 0)
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            cur = node.val + left[1] + right[1]
            befor = max(left) + max(right)
            
            return (cur, befor)
        
        return max(traverse(root))