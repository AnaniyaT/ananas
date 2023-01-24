class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mydict = {}
        for ind, num in enumerate(numbers):
            if target - num in mydict:
                return [mydict[target-num]+1, ind+1]
            mydict[num] = ind