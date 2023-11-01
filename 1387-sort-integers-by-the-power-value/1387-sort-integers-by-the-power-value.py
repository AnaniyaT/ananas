class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getScore(num):
            if num == 1:
                return 0
            
            mod = num % 2
            if mod:
                return getScore(num * 3 + 1) + 1
            
            return getScore(num // 2) + 1
        
        nums = [num for num in range(lo, hi + 1)]
        nums.sort(key=getScore)
        
        return nums[k-1]