# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        tree = None
        
        def insert(val):
            nonlocal tree
            
            if not tree:
                tree = TreeNode(val)
                return
            
            curr = tree
            while True:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = TreeNode(val)
                        return

                else:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = TreeNode(val)
                        return
                    
        for num in preorder:
            insert(num)
            
        return tree