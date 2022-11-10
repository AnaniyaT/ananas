class Solution:
    def removeDuplicates(self, s: str) -> str:
        stak = [""]
        for i in s:
            if stak[-1] == i:
                stak.pop()
            else:
                stak.append(i)
        return "".join(stak)