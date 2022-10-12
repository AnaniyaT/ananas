class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = l =  0
        summ = sum(arr[:k])
        if summ/k >= threshold:
            count += 1
        for r in range(k, len(arr)):
            summ += arr[r]
            summ -= arr[l]
            l += 1
            if summ/k >= threshold:
                count += 1
        return count