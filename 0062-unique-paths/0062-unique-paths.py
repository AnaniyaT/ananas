class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = n - 1
        d = m - 1
        
        return factorial(r + d) // (factorial(r) * factorial(d))
