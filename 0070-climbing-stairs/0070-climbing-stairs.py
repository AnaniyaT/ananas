class Solution(object):
    dp = [1,2]
    def climbStairs(self, n):
        if n <= len(self.dp):
            return self.dp[n-1]
        self.dp.append(self.climbStairs(n-1) + self.climbStairs(n-2))
        return self.dp[n-1]
            