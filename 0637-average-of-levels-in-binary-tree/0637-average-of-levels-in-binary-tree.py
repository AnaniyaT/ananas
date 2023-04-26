# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        
        queue = deque([(1, root)])
        
        while queue:
            lvl, curr = queue.pop()
            
            if lvl > len(levels):
                levels.append([1, curr.val])
            else:
                levels[lvl - 1][0] += 1
                levels[lvl - 1][1] += curr.val
            
            if curr.left:
                queue.appendleft((lvl + 1, curr.left))
            if curr.right:
                queue.appendleft((lvl + 1, curr.right))
            
                      
        return list(map(lambda x: x[1] / x[0], levels))
            