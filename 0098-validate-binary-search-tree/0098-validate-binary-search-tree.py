# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(upper, lower, node):
            if not node:
                return True
            
            val = node.val
            
            if val >= upper or val <= lower:
                return False
            
            left = validate(min(upper, val), lower, node.left)
            right = validate(upper, max(lower, val), node.right)
            
            return left and right
        
        return validate(float('inf'), -float('inf'), root)
