class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0] * k
        length = len(cookies)
        optimalDist = float('inf')
        
        def distribute(ind):
            nonlocal optimalDist,k , length
            
            if ind >= length:
                optimalDist = min(optimalDist, max(dist))
                return
                
            for indx in range(k):
                dist[indx] += cookies[ind]
                
                if dist[indx] >= optimalDist:
                    dist[indx] -= cookies[ind]
                    continue
                    
                distribute(ind + 1)
                
                dist[indx] -= cookies[ind]
        
        distribute(0)
                
        return optimalDist
                