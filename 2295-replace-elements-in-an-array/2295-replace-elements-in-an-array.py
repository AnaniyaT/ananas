class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indDict = {}
        
        for ind, num in enumerate(nums):
            indDict[num] = ind
            
        for operation in operations:
            oldNum = operation[0]
            newNum = operation[1]
            ind = indDict[oldNum]
            nums[ind] = newNum
            indDict.pop(oldNum)
            indDict[newNum] = ind
            
        return nums