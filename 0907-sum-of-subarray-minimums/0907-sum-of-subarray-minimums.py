class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        minSum = 0
        
        for ind in range(len(arr) + 1):
            while stack and (ind == len(arr) or arr[stack[-1]] >= arr[ind]):
                prev = stack.pop()
                left = -1 if not stack else stack[-1]
                
                minSum += arr[prev] * (prev-left) * (ind-prev)
                
            stack.append(ind)
            
        mod = 1000000007
        
        return minSum % mod