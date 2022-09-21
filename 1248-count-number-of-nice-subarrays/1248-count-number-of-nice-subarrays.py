class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        precount = count = 0
        for i in nums:
            if i%2:
                precount += 1
            if precount not in dic:
                dic[precount] = 1
            else:
                dic[precount] += 1
            count += dic.get(precount-k,0)
        return count