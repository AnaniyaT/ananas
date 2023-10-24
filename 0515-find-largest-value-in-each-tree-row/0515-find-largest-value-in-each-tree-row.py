# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largests = []
        
        queue = deque()
        
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            maxx = -float('inf')
            for _ in range(size):
                cur = queue.pop()
            
                maxx = max(maxx, cur.val)
                if cur.left:
                    queue.appendleft(cur.left)
                if cur.right:
                    queue.appendleft(cur.right)
                
            largests.append(maxx)
        
        return largests