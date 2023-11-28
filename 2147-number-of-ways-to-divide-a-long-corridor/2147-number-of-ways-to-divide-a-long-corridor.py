class Solution:
    def numberOfWays(self, corridor: str) -> int:
        s = Counter(corridor)["S"]
        if not s or s % 2:
            return 0
        
        seats = 0
        ways = 1
        mod = 10 ** 9 + 7
        plants = 0
        for cell in corridor:
            if cell == "S":
                seats += 1
                if seats == 3:
                    seats = 1
                    ways *= plants + 1
                    ways %= mod
                    plants = 0
            elif cell == "P":
                if seats == 2:
                    plants += 1
                    
        return ways
                    
            
            