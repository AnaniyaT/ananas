class Solution:
    def reverseString(self, s: List[str], p=0) -> None:
        if p >= len(s)//2:
            return
        
        s[p], s[~p] = s[~p], s[p]
        self.reverseString(s, p+1)
        