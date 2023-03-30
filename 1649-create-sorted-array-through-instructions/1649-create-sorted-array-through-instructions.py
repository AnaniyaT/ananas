from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        
        cost = 0
        for num in instructions:
            less = nums.bisect_left(num)
            greater = len(nums) - nums.bisect_right(num)
            
            cost += min(less, greater)
            nums.add(num)
            
        return cost % 1_000_000_007