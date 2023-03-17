class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = [0]
        count = Counter(tiles)
        
        def backtrack(n):
            if not n:
                sequences[0] += 1
                        
                return
            
            
            for lett in count:
                if not count[lett]:
                    continue
                
                count[lett] -= 1
                backtrack(n - 1)
                count[lett] += 1
                
                
        for lens in range(1, len(tiles)+1):
            backtrack(lens)
        
        return sequences[0]