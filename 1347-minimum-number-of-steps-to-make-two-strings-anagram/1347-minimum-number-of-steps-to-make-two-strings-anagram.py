class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countA = Counter(s)
        countB = Counter(t)
        n = len(s)
        steps = 0
        
        for ch in countA:
            steps += min(countA[ch], countB[ch])
            
        return n - steps