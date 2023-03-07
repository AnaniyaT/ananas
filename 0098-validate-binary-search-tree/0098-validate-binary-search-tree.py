# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], maxx=float('inf'), minn=-float('inf')) -> bool:
        if not root:
            return True
        
        val = root.val
        
        if val >= maxx:
            return False
        
        if val <= minn:
            return False
        
        
        left = self.isValidBST(root.left, val, minn)
        right = self.isValidBST(root.right, maxx, val)
        
        return left and right