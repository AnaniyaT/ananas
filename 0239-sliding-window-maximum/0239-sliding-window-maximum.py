class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        
        for idx in range(k):
            while queue and nums[queue[-1]] <= nums[idx]:
                queue.pop() 
            queue.append(idx)
            
        ans = [nums[queue[0]]]
        l = 0
        for r in range(k, len(nums)):
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            queue.append(r)
            
            if l == queue[0]:
                queue.popleft()
                
            l += 1
            
            ans.append(nums[queue[0]])
            
        return ans
            