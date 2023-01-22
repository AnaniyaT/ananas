class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        for ind in range(len(arr)):
            currNum = arr[~ind]
            arr[~ind] = maxx
            maxx = max(maxx, currNum)
            
        return arr