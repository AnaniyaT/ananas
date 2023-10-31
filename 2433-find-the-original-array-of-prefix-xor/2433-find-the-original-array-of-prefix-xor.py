class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        pref.append(0)
        ans = []
        
        for idx in range(len(pref) - 1):
            ans.append(pref[idx] ^ pref[idx-1])
        
        return ans