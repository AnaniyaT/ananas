# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        
        def traverse(tree, col=0, row=0):
            if not tree:
                return 
            
            columns[col].append((row, tree.val))
            
            traverse(tree.left, col-1, row+1)
            traverse(tree.right, col+1, row+1)
            
        traverse(root)
        
        answer = []
        
        for col in sorted(columns):
            answer.append(list(map(lambda x: x[1], (sorted(columns[col])))))
            
        return answer
            
            