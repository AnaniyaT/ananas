class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        maxx = max(nums)
        n = len(nums)
        
        def check(diff):
            found = defaultdict(int)
            
            for num in nums:
                found[num] = found[num - diff] + 1
                
            # print(diff, found)
            return max(found.values())
        
        ans = 1
        for diff in range(-(maxx) ,maxx + 1):
            res = check(diff)
            if res > ans:
                ans = res
                # print(diff, res)
            
        return ans
            
            
            