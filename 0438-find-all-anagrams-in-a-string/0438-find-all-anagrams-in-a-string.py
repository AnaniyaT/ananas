class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = [0] * 26
        s_counter = [0] * 26
        for char in p:
            p_counter[ord(char) - ord('a')] += 1
        for i in range(len(s)):
            s_counter[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                s_counter[ord(s[i - len(p)]) - ord('a')] -= 1
            if s_counter == p_counter:
                result.append(i - len(p) + 1)
                
        return result
