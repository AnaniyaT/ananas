class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        length = len(spaces)
        spacePtr = 0
        for ind, char in enumerate(s):
            if spacePtr < length and ind == spaces[spacePtr]:
                result.append(" ")
                spacePtr += 1
            result.append(char)
            
        return "".join(result)