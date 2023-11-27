class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxx = 0
        subs = 0
        for idx in range(len(arr)):
            maxx = max(maxx, arr[idx])
            if maxx <= idx:
                subs += 1
                
        return subs