# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        paths = 0
        
        def traverse(currSum, node):
            nonlocal targetSum, paths
            
            if not node:
                return
            
            currSum += node.val
            paths += prefix[currSum - targetSum]
            
            prefix[currSum] += 1
            
            traverse(currSum, node.left)
            traverse(currSum, node.right)
            
            prefix[currSum] -= 1
            if not prefix[currSum]:
                prefix.pop(currSum)
                
        traverse(0, root)
        
        return paths
            