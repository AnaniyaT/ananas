class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indxdic = {}
        for i, j in enumerate(nums):
            if target-j in indxdic:
                return [i, indxdic[target-j]]
            else:
                indxdic[j] = i