class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        goodPairs = 0
        for num in nums:
            if num in count:
                goodPairs += count[num]
                count[num] += 1
            else:
                count[num] = 1
        return goodPairs     