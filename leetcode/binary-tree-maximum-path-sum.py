# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float('inf')
        
        def dfs(node):
            nonlocal maxSum
            
            if not node:
                return -float('inf')
            
            left = dfs(node.left)
            right = dfs(node.right)
            val = node.val
            
            maxSum = max(maxSum, val, val + left, val + right, val + left + right)
            
            return max(val, val + left, val + right)
            
            
        dfs(root)
        
        return maxSum
        
        
        
        