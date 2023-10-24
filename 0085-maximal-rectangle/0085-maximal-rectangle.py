class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        pref = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == "1":
                    pref[r][c] = pref[r][c-1] + 1
                   
        maxArea = 0
        for c in range(m):
            for r in range(n):
                w = pref[r][c]
                for er in range(r, n):
                    if not pref[er][c]:
                        break
                    
                    w = min(w, pref[er][c])
                    maxArea = max(maxArea, w * (er - r + 1))
                    
                    
        return maxArea