# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def toNum(lst):
            num = 0
            while lst:
                num *= 10
                num += lst.val
                lst = lst.next
                
            return num
        
        num1 = toNum(l1)
        num2 = toNum(l2)
        
        add = num1 + num2
        
        if not add:
            return ListNode(0)
        
        newLst = None
        while add:
            cur = ListNode(add%10)
            cur.next = newLst
            newLst = cur
            add //= 10
            
        return newLst