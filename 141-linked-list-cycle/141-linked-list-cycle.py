# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slownode = head
        fastnode = head
        while slownode.next != None:
            slownode = slownode.next
            if fastnode == None or fastnode.next == None:
                return False
            fastnode = fastnode.next.next
            if slownode == fastnode:
                return True
        return False