class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        count = summ = 0
        for i in nums:
            summ += i
            count += dic.get(summ-k,0)
            if summ in dic:
                dic[summ] += 1
            else:
                dic[summ] = 1
                
        return count