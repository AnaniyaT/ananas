# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        answer = []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            level = []
            
            for _ in range(size):
                curr = queue.pop()
                level.append(curr.val)
                
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
                    
            answer.append(level)
        
        return answer