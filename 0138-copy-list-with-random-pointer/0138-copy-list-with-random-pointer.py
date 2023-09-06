"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        indices = {}
        nodes = {}
        newNodes = {}
        
        indices[str(None)] = 1001
        
        nodes[1001] = None
        newNodes[1001] = None
        
        newList = Node(0)
        
        cur = head
        newCur = newList
        idx = 0
        
        while cur:
            indices[str(cur)] = idx
            nodes[idx] = cur
            newCur.next = Node(cur.val)
            newNodes[idx] = newCur.next
            newCur = newCur.next
            cur = cur.next
            idx += 1
        
        cur = head
        newCur = newList.next
        
        while cur:
            newCur.random = newNodes[indices[str(cur.random)]]
            cur = cur.next
            newCur = newCur.next
            
        # cur = newList.next
        # while cur:
        #     print(cur.val, end="-")
        #     print(cur.random.val if cur.random else "null")
        #     cur = cur.next
            
        return newList.next
            
        
        