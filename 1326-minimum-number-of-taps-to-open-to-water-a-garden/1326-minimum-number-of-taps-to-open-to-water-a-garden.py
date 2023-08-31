class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        def coveres(i, j):
            if ranges[j] == 0:
                return False
            
            return j - ranges[j] <= i < j + ranges[j]
        
        cur = -1
        req = 0
        for idx in range(n):
            if idx > cur:
                found = -1
                for off in range(101):
                    if idx + off > n:
                        break
                    if coveres(idx, idx + off):
                        found = idx + off
                        cur = max(cur, found + ranges[found] - 1)
                        
                for off in range(101):
                    if idx - off < 0:
                        break
                    if coveres(idx, idx - off):
                        found = idx - off
                        cur = max(cur, found + ranges[found] - 1)
                
                if found == -1:
                    return -1
                
                req += 1
                
        return req