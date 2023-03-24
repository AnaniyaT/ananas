class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        curr = [0] * n
        fulfilled = 0
        maxRequests = 0
        length = len(requests)
        
        def backtrack(ind):
            nonlocal maxRequests, length, fulfilled, n
            
            if ind == length or fulfilled + (length - ind) <= maxRequests:
                if all([not curr[ind] for ind in range(n)]):
                    maxRequests = max(maxRequests, fulfilled)
                    
                return
            
            fro, to = requests[ind]
            
            curr[fro] -= 1
            curr[to] += 1
            fulfilled += 1
            
            backtrack(ind + 1)
            
            curr[fro] += 1
            curr[to] -= 1
            fulfilled -= 1
            
            backtrack(ind + 1)
            
        backtrack(0)
        
        return maxRequests
            