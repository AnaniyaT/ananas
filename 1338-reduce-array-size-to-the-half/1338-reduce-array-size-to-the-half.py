class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        freqlist = sorted(freq, key = freq.get, reverse = True)
        acc = 0
        half = len(arr)//2
        n = 0
        for i in freqlist:
            if acc <  half:
                acc += freq[i]
                n += 1
            else:
                return n
        return 1