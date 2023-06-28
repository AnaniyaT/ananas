# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict(lambda: None)
        
        def find(prev, node):
            if not node:
                return False
            
            val = node.val
            
            if val == target.val:
                parent[val] = prev
                return True
            
            left = find(node, node.left)
            right = find(node, node.right)
            
            if left or right:
                parent[val] = prev
                return True
            
            return False
                
        find(None, root)
        
        queue = deque([target])
        visited = set([target.val])
        s = 0
        
        while s < k and queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop()
                
                if cur.left and cur.left.val not in visited:
                    visited.add(cur.left.val)
                    queue.appendleft(cur.left)
                
                if cur.right and cur.right.val not in visited:
                    visited.add(cur.right.val)
                    queue.appendleft(cur.right)
                    
                par = parent[cur.val]
                if par and par.val not in visited:
                    visited.add(par.val)
                    queue.appendleft(par)
                    
            s += 1
            
        if s == k:
            ans = []
            while queue:
                ans.append(queue.pop().val)
            
            return ans
        else:
            return []
        
        