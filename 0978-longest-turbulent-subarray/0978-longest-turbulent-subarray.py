class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 1
        
        prev = -1
        curLen = 1
        
        for ind in range(1, len(arr)):
            less = int(arr[ind] < arr[ind-1])
            if arr[ind] == arr[ind-1]:
                curLen = 1
                prev = -1
            
            elif less == prev:
                curLen = 2
            
            else:
                curLen += 1
                prev = less
                
            maxLen = max(maxLen, curLen)
            
        return maxLen
                
        
        
                
        
        