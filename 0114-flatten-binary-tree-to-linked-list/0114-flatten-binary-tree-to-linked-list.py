# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        
        def trav(node):
            if not node.left and not node.right:
                return node
            
            if not node.left:
                return trav(node.right)
            
            left = trav(node.left)
            right = node.right
            node.right = node.left
            
            node.left = None
            
            if not right:
                return left
            
            left.right = right
            
            return trav(right)
        
        trav(root)
            
            
            
            
            