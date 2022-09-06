# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        currNode = head
        while currNode.next:
            if currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        return head
                
        