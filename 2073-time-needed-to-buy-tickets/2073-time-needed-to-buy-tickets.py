class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         queue = deque(tickets)
#         count = 0
        
#         while True:
#             queue[0] -= 1
#             temp = queue.popleft()
#             if temp:
#                 queue.append(temp)
            
#             if not(temp or k):
#                 return count+1
            
#             k -= 1
#             if k == -1:
#                 k = len(queue)-1
            
#             count += 1
        
        timeTaken = 0
        kth = tickets[k]
        
        for ind, num in enumerate(tickets):
            if ind < k:
                timeTaken +=  min(num, kth)
            elif ind > k:
                timeTaken += min(num, kth-1)
                
        return timeTaken + kth
            
            
            
            
        