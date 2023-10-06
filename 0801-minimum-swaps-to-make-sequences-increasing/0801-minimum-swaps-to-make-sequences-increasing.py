class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @cache
        def dfs(prev, ind):
            if ind == n:
                return 0
            
            pn1, pn2 = prev
            num1, num2 = nums1[ind], nums2[ind]
            
            ans = float('inf')
            
            if pn1 < num1 and pn2 < num2:
                ans = min(ans, dfs((num1, num2), ind + 1))
            
            if pn2 < num1 and pn1 < num2:
                ans = min(ans, dfs((num2, num1), ind + 1) + 1)
            
            return ans
        
        return dfs((-1, -1), 0)
                
            
            