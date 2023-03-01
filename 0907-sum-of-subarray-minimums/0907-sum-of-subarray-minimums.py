class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        before = [i for i in range(len(arr))]
        after = [i for i in range(len(arr)-1, -1, -1)]
        
        stack = []
        for ind, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                after[stack[-1]] = ind - stack[-1] -1
                stack.pop()
                
            stack.append(ind)
            
        for ind in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] > arr[ind]:
                before[stack[-1]] = stack[-1] - ind - 1
                stack.pop()
                
            stack.append(ind)
        
        minSum = 0
        for ind in range(len(arr)):
            subArrays = before[ind] + after[ind] + (before[ind]*after[ind]) + 1
            minSum += arr[ind]*subArrays
            
        mod = 1000000007
        
        return minSum % mod