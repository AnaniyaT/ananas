class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i,j in enumerate(l):
            arr = nums[j:r[i]+1]
            if len(arr) == 2:
                ans.append(True)
                continue
            arr = sorted(arr)
            d = arr[1] - arr [0]
            for i in range (2,len(arr)):
                if i!=len(arr)-1 and arr[i] - arr[i-1] == d:
                    continue
                elif i == len(arr)-1 and arr[i] - arr[i-1] == d:
                    ans.append(True)
                else:
                    ans.append(False)
                    break 
        return ans