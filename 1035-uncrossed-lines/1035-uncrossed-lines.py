class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        @cache
        def dfs(i1, i2):
            if i1 >= l1 or i2 >= l2:
                return 0
            
            cur = nums1[i1]
            
            ans = 0
            
            for ind in range(i2, l2):
                if cur == nums2[ind]:
                    ans = max(ans, dfs(i1 + 1, ind + 1) + 1)
                    
            ans = max(ans, dfs(i1 + 1, i2))
            
            return ans
        
        return dfs(0, 0)