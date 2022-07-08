class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counterlist = sorted(counter, key=counter.get, reverse=True)
        return counterlist[:k]
    
        