class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)-1
        for ind, num in enumerate(numbers):
            while num+numbers[r] > target:
                r -= 1
        
            if num+numbers[r] == target:
                return [ind+1, r+1]