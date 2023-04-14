# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totSum = 0
        
        def dfs(node, curr=0):
            nonlocal totSum
            
            curr = curr * 10 + node.val
            
            if not node.left and not node.right:
                totSum += curr
                return
            
            if node.left:
                dfs(node.left, curr)
            
            if node.right:
                dfs(node.right, curr)
            
        dfs(root)
        
        return totSum