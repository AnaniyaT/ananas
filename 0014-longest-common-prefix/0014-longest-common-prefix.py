class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commPre = ""
        minLen = min(list(map(len, strs)))
        for _ in range(minLen):
            ind = len(commPre)
            candidate = strs[0][ind]
            for word in strs:
                if word[ind] != candidate:
                    return commPre
            commPre += candidate
        return commPre
                    