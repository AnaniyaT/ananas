# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def dfs(node, p, q):
            nonlocal ans
            
            if ans:
                return False, False
            
            if not node:
                return False, False
            
            pl, ql = dfs(node.left, p, q)
            pr, qr = dfs(node.right, p, q)
            
            pp = node.val == p or pl or pr
            qq = node.val == q or ql or qr
            
            if pp and qq:
                ans = node
                return False, False
            
            return pp, qq
        
        dfs(root, p.val, q.val)
        
        return ans