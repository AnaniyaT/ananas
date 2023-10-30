class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removed = set()
        
        stk = []
        for idx in range(len(s)):
            if s[idx] == "(":
                stk.append(idx)
            elif s[idx] == ")":
                if stk:
                    stk.pop()
                else:
                    removed.add(idx)
                    
        while stk:
            removed.add(stk.pop())
            
        ans = []
        for idx in range(len(s)):
            if idx not in removed:
                ans.append(s[idx])
                
        return "".join(ans)