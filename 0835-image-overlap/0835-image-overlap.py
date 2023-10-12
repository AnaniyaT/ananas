class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        maxOverlap = 0
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n
        
        for x in range(-(n-1), n):
            for y in range((-n-1), n):
                overlap = 0
                for r in range(n):
                    for c in range(n):
                        sr, sc = r + x, c + y
                        if isValid(sr, sc):
                            if img1[sr][sc] and img1[sr][sc] == img2[r][c]:
                                overlap += 1
                                
                maxOverlap = max(maxOverlap, overlap)
                
        return maxOverlap