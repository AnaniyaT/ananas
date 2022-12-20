class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS = Counter(s)
        counterT = Counter(t)
        for letter in counterT:
            if letter not in counterS or counterS[letter] < counterT[letter]:
                return letter