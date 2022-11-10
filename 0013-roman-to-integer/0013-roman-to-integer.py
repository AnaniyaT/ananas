class Solution:
    def romanToInt(self, s: str) -> int:
        valdic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        for i, j in enumerate(s):
            if i != len(s)-1 and j=="I" and s[i+1] in ["V","X"]:
                result -= valdic[j]
            elif i != len(s)-1 and j=="X" and s[i+1] in ["L","C"]:
                result -= valdic[j]
            elif i != len(s)-1 and j=="C" and s[i+1] in ["D","M"]:
                result -= valdic[j]
            else:
                result += valdic[j]
        return result