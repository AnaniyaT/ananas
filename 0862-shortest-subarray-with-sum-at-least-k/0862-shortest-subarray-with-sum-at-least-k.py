class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        maxQ = deque([(0,-1)])
        
        minLen = float('inf')
        runSum = 0
        
        for ind, num in enumerate(nums):
            runSum += num
            while maxQ and maxQ[-1][0] > runSum:
                maxQ.pop()

            maxQ.append((runSum, ind))
            
            while runSum - maxQ[0][0] >= k:
                length = ind - maxQ[0][1]
                minLen = min(minLen, length)
                maxQ.popleft()
                
        if minLen == float('inf'):
            return -1
        else:
            return minLen
                