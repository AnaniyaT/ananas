class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {1:0}
        def getScore(num):
            nonlocal dp
            if num in dp:
                return dp[num]
            
            mod = num % 2
            score = 0
            if mod:
                score += getScore(num * 3 + 1) + 1
            else:
                score += getScore(num // 2) + 1
                
            dp[num] = score
            return score
        
        nums = [num for num in range(lo, hi + 1)]
        nums.sort(key=getScore)
        
        return nums[k-1]