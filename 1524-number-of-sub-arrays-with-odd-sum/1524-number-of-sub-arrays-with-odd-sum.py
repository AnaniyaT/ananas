class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even, odd = 1, 0
        subArrays = 0
        
        runSum = 0
        for num in arr:
            runSum += num
            if runSum % 2:
                subArrays += even
                odd += 1
            else:
                subArrays += odd
                even += 1
                
        mod = 1_000_000_007
        
        return subArrays % mod