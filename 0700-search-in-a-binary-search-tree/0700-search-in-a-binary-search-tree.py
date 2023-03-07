# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#        if not root:
#        return None
        
#         value = root.val
        
#         if value == val:
#             return root
        
#         if value > val:
#             return self.searchBST(root.left, val)
        
#         return self.searchBST(root.right, val)

        curr = root
    
        while curr:
            value = curr.val
            
            if value == val:
                return curr
            elif value > val:
                curr = curr.left
            else:
                curr = curr.right
                
        return curr