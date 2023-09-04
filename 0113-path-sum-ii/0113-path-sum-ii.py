# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        
        if not root:
            return []
        
        def traverse(node, summ, path):
            path.append(node.val)
            
            if not node.left and not node.right:
                if summ + node.val == targetSum:
                    paths.append(path[:])
            
            if node.left:
                traverse(node.left, summ + node.val, path)
            if node.right:
                traverse(node.right, summ + node.val, path)
                
            path.pop()
            
        traverse(root, 0, [])
        
        return paths