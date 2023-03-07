# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinRight(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
            
        return curr
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            minRight = self.findMinRight(root.right).val
            
            root.val = minRight
            
            root.right = self.deleteNode(root.right, minRight)
            
        return root
        
        