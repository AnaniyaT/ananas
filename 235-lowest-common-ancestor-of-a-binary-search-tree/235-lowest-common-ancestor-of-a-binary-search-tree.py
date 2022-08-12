# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval = p.val
        qval = q.val
        currNode = root
        while currNode.left != None or currNode.right != None:
            if pval <= currNode.val and qval >= currNode.val:
                return currNode
            elif pval >= currNode.val and qval <= currNode.val:
                return currNode
            elif pval <= currNode.val and qval <= currNode.val:
                currNode = currNode.left
            else:
                currNode = currNode.right