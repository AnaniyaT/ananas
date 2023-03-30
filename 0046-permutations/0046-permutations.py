class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = 0
        length = len(nums)
        perms = []
        curr = []
        
        def backtrack(ind):
            nonlocal length, used
            
            if not ind:
                if len(curr) == length:
                    perms.append(curr[:])
                return
            
            for i in range(length):
                shift = 1 << i
                if not (used & shift):
                    curr.append(nums[i])
                    used ^= shift
                    backtrack(ind - 1)
                    used ^= shift
                    curr.pop()
                    backtrack(ind - 1)
                    
        backtrack(length)
        
        return perms
                    
                