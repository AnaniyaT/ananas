# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def findSum(tree):
            nonlocal count
            if not tree:
                return 0, 0
            
            leftSum, leftNum = findSum(tree.left)
            rightSum, rightNum = findSum(tree.right)
            
            summ = tree.val + leftSum + rightSum
            num = leftNum + rightNum + 1
            average = summ // num
            
            if average == tree.val:
                count += 1
                
            return summ, num
        
        findSum(root)
        
        return count