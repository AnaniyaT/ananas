class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        dic = Counter(p)
        l = r = 0
        result = []
        while r < len(p):
            if s[r] in dic:
                dic[s[r]] -= 1
            r += 1
        if all(c == 0 for c in dic.values()):
            result.append(l)
        while r < len(s):
            if s[l] in dic:
                dic[s[l]] += 1
            if s[r] in dic:
                dic[s[r]] -= 1
            r += 1
            l += 1
            if all(c == 0 for c in dic.values()):
                result.append(l)
        return result