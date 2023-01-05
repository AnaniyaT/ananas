class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearrangedArray = [0 for _ in range (len(nums))]
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                rearrangedArray[pos] = num
                pos += 2
            else:
                rearrangedArray[neg] = num
                neg += 2
        
        return rearrangedArray
                