# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        currNode = head
        currVal = head.val
        while currNode.next:
            if currNode.next.val == currVal:
                currNode.next = currNode.next.next
            else:
                currVal = currNode.next.val
                currNode = currNode.next
        return head
                
        