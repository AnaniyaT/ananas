# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        
        traversal = []
        
        while queue:
            node, lvl = queue.pop()
            if node.left:
                queue.appendleft((node.left, lvl + 1))
            
            if node.right:
                queue.appendleft((node.right, lvl + 1))
                
            if lvl == len(traversal):
                traversal.append([])
                
            traversal[lvl].append(node.val)
            
        return list(reversed(traversal))
            
            