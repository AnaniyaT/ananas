# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temphead = ListNode(None, head)
        prev, curr = head, head.next
        while prev and curr:
            if curr.val < prev.val:
                insertafter = temphead
                while insertafter.next.val < curr.val:
                    insertafter = insertafter.next
                prev.next = curr.next
                curr.next = insertafter.next
                insertafter.next = curr
                curr = prev.next
            else:
                prev, curr = prev.next, curr.next
                
        return temphead.next
        