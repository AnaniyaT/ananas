# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(tree):
            if not tree:
                return True, float('inf'), -float('inf')

            val = tree.val

            left, leftMin, leftMax = isValid(tree.left)
            right, rightMin, rightMax = isValid(tree.right)

            if val <= leftMax or val >= rightMin:
                return False, -float('inf'), float('inf')

            return left and right,min(val, leftMin), max(rightMax, val)
        
        return isValid(root)[0]