# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval, qval = p.val, q.val
        
        if max(pval, qval) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if min(pval, qval) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
    
#         currNode = root
        
#         while currNode.left or currNode.right:
#             if max(p.val,q.val) < currNode.val:
#                 currNode = currNode.left
                
#             elif min(p.val,q.val) > currNode.val:
#                 currNode = currNode.right
                
#             else:
#                 return currNode