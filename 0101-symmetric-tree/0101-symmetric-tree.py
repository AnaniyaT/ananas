# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            
            if not(tree1 and tree2) or tree1.val != tree2.val:
                return False
            
            left = isSameTree(tree1.left, tree2.right)
            right = isSameTree(tree1.right, tree2.left)
            
            return left and right
        
        return isSameTree(root.left, root.right)