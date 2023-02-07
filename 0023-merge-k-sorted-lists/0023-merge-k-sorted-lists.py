# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         newList = ListNode(0)
#         newCurr = newList
        
#         isNotEmpty = True
        
#         while isNotEmpty:
#             minn = [float('inf'), -1]
            
#             for ind, lst in enumerate(lists):
#                 if lst and lst.val < minn[0]:
#                     minn = [lst.val, ind]
            
#             if minn[0] != float('inf'):
#                 newCurr.next = ListNode(minn[0])
#                 newCurr = newCurr.next
#                 lists[minn[1]] = lists[minn[1]].next
#             else:
#                 isNotEmpty = False
                
#         return newList.next

        heap = []
        heapq.heapify(heap)
        
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next
                
        newList = ListNode(0)
        curr = newList
        
        while heap:
            val = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            
        return newList.next
        