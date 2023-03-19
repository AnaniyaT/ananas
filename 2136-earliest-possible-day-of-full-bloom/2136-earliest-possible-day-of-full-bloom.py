class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        indices = [ind for ind in range(len(growTime))]
        indices.sort(reverse=True, key=lambda x: growTime[x])
        
        curr = 0
        maxTime = 0
        
        for ind in indices:
            curr += plantTime[ind]
            maxTime = max(maxTime, curr + growTime[ind])
            
        return maxTime
        