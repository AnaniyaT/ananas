class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            mySet.add(num)
            revNum = int(str(num)[::-1])
            mySet.add(revNum)
            
        return len(mySet)