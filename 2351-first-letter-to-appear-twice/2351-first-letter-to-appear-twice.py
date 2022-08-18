class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sett = []
        for i in s:
            if i in sett:
                return i
            else:
                sett.append(i)