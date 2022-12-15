class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2) + 1)]
        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1) - 1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]