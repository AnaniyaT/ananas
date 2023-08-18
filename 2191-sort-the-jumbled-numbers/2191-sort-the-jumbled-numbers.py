class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def getVal(num):
            if not num:
                return mapping[num]
            res = 0
            times = 1
            while num:
                res += mapping[num % 10] * times
                times *= 10
                num //= 10
                
            return res
        
        nums.sort(key=getVal)
        return nums
                
#         mappedNums = []
#         for ind, num in enumerate(nums):
#             mappedNums.append((getVal(num), ind))
            
#         mappedNums.sort()
#         print(mappedNums)
#         return list(map(lambda x: nums[x[1]], mappedNums))
                
    