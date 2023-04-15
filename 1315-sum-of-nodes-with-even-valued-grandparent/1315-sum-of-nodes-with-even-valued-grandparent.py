# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        _sum = 0
        
        def dfs(node, p, gp):
            nonlocal _sum
            
            if not node:
                return
            
            if not gp % 2:
                _sum += node.val
                
            # current node becomes parent and parent becomes grand parent
            dfs(node.left, node.val, p)
            dfs(node.right, node.val, p)
            
        dfs(root, 1, 1)
        
        return _sum