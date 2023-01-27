class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operations = 0
        for num in count:
            target = k-num
            if num == target:
                operations += count[num]//2
            elif target in count:
                operations += min(count[num], count[target])
                count[target] = 0
            
        return operations