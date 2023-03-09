# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxSum = 0
        
        def isValid(tree):
            nonlocal maxSum
            if not tree:
                return True, float('inf'), -float('inf'), 0

            val = tree.val

            left, leftMin, leftMax, leftSum = isValid(tree.left)
            right, rightMin, rightMax, rightSum = isValid(tree.right)

            if val <= leftMax or val >= rightMin:
                return False, -float('inf'), float('inf'), 0
            
            maxSum = max(maxSum, leftSum + rightSum + val)
            
            return left and right,min(val, leftMin), max(rightMax, val), leftSum + rightSum + val
    
        isValid(root)
            
        return maxSum
            
            
            
            