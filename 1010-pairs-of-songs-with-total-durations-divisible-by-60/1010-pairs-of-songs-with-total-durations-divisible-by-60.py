class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        pairs = 0
        for song in time:
            mod = song%60
            pairs += count[60-mod]
            if not mod:
                count[60] += 1
            count[mod] += 1
        
        return pairs
            