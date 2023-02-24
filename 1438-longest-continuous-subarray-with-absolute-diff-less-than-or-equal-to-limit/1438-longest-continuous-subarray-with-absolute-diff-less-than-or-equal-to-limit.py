class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxx = deque([-float('inf')])
        minn = deque([float('inf')])
        
        maxLen = 0
        l = 0
        
        for r in range(len(nums)):
            while maxx and maxx[-1] < nums[r]:
                maxx.pop()
            
            while minn and minn[-1] > nums[r]:
                minn.pop()
                
            minn.append(nums[r])
            maxx.append(nums[r])
            
            while maxx[0] - minn[0] > limit:
                if nums[l] == maxx[0]:
                    maxx.popleft()
                elif nums[l] == minn[0]:
                    minn.popleft()
                    
                l += 1
                
            maxLen = max(maxLen, r-l+1)
            
        return maxLen
                
            
                    