# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currNode = root
        while currNode.left != None or currNode.right != None:
            if p.val <= currNode.val and q.val >= currNode.val:
                return currNode
            elif p.val >= currNode.val and q.val <= currNode.val:
                return currNode
            elif p.val <= currNode.val and q.val <= currNode.val:
                currNode = currNode.left
            else:
                currNode = currNode.right