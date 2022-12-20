class Solution:
    def similarPairs(self, words: List[str]) -> int:
        countDic = {}
        for word in words:
            letters = list(set(word))
            letters = sorted(letters, key=ord)
            lettersStr = "".join(letters)
            if lettersStr in countDic:
                countDic[lettersStr] += 1
            else:
                countDic[lettersStr] = 1
        pairs = 0
        for key in countDic:
            count = countDic[key]
            pairs += (count*(count-1))//2
        return pairs
            