# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(lambda: [float(inf), -float(inf)])
        maxWidth = 0
        
        def traverse(tree, lvl=0, col=1):
            nonlocal maxWidth
            
            if not tree:
                return 
            
            levels[lvl][0] = min(levels[lvl][0], col)
            levels[lvl][1] = max(levels[lvl][1], col)
            
            maxWidth = max(maxWidth, levels[lvl][1] - levels[lvl][0] + 1)
            
            traverse(tree.left, lvl+1, (col*2)-1)
            traverse(tree.right, lvl+1, col*2)
            
            
        traverse(root)
        
        return maxWidth

# bfs version

# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         queue = deque([(0, root)])
#         maxWidth = 1
        
#         while queue:
#             size = len(queue)
#             leftMost = float('inf')
#             rightMost = -float('inf')
            
#             for _ in range(size):
#                 ind, node = queue.pop()
#                 leftMost = min(leftMost, ind)
#                 rightMost = max(rightMost, ind)
                
#                 if node.left:
#                     queue.appendleft((ind * 2, node.left))
#                 if node.right:
#                     queue.appendleft((ind * 2 + 1, node.right))
                    
#             maxWidth = max(maxWidth, rightMost - leftMost + 1)
            
#         return maxWidth
            
            
        
