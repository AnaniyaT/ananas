class Solution:
    def knightDialer(self, n: int) -> int:
        graph = [
            [4, 6],
            [8, 6],
            [7, 9],
            [4, 8],
            [3, 0, 9],
            [],
            [1, 7, 0],
            [6, 2],
            [1, 3],
            [4, 2],
            [4, 6]
        ]
        
        mod = 1_000_000_007
        
        @cache
        def dp(num, n):
            if not n:
                return 1
            
            ans = 0
            for neigh in graph[num]:
                ans += dp(neigh, n-1)
                ans %= mod
            
            return ans
        
        ans = 0
        for num in range(10):
            ans += dp(num, n-1)
            ans %= mod
            
        return ans
        