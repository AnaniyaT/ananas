class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def isValid(r, c, clr):
            return (0 <= r < len(image)) and (0 <= c < len(image[0])) and image[r][c] == clr
        
        visited = set()
        def dfs(r, c):
            clr = image[r][c]
            image[r][c] = color
            visited.add((r, c))
            
            for rOff, cOff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r + rOff, c + cOff
                if isValid(newR, newC, clr) and (newR, newC) not in visited:
                    dfs(newR, newC)
                    
        dfs(sr, sc)
        
        return image
            