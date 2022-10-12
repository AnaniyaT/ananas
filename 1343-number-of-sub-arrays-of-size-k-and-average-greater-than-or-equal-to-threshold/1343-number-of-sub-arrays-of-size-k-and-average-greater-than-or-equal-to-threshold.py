class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = l =  0
        s = threshold*k
        summ = sum(arr[:k])
        if summ >= s:
            count += 1
        for r in range(k, len(arr)):
            summ += arr[r]
            summ -= arr[l]
            l += 1
            if summ >= s:
                count += 1
        return count