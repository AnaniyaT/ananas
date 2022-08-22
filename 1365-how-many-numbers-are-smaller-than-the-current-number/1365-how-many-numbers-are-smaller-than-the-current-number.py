class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        myDic = {}
        for i in range(len(nums)-1, -1, -1):
            myDic[sortedNums[i]] = i
        result = []
        for j in nums:
            result.append(myDic[j])
        return result
            
            
                    