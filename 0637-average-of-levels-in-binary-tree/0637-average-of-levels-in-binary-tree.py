# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        answer = []
        
        while queue:
            size = len(queue)
            summ = 0
            
            for _ in range(size):
                curr = queue.pop()
                summ += curr.val
                
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
            
            answer.append(summ / size)
                      
        return answer
            