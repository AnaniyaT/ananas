class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        ind = 0
        while ind < len(s):
            if ind < len(s) - 2 and s[ind+2] == "#":
                result.append(chr(int(s[ind:ind+2])+96))
                ind += 3
            else:
                result.append(chr(int(s[ind])+96))
                ind += 1
        return "".join(result)