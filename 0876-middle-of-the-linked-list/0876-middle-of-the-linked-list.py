# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast.next:
            if not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            return slow.next
        return slow
        