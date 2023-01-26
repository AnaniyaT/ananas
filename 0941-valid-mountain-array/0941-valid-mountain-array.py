class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        r = len(arr)-1
        while r > 0 and arr[r] < arr[r-1]:
            r -= 1
        for ind in range(len(arr)-1):
            if arr[ind] >= arr[ind+1]:
                return ind == r and r != 0 and r != len(arr)-1
            