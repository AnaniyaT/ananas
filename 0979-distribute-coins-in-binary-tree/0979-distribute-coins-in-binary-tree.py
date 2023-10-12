# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ops = 0
        
        def trav(node):
            nonlocal ops
            
            if not node:
                return 0
            
            node.val += trav(node.left)
            node.val += trav(node.right)
            
            ops += abs(1 - node.val)
            return node.val - 1
        
        
        trav(root)
            
        return ops