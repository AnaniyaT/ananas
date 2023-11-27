class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedd = sorted(arr)
        
        s1, s2 = set(), set()
        
        subs = 0
        for idx in range(len(arr)):
            s1.add(sortedd[idx])
            s2.add(arr[idx])
            if s1 == s2:
                subs += 1
                
        return subs