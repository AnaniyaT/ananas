class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check(parenthesis):
            count = 0
            for p in parenthesis:
                if p == "(":
                    count += 1
                else:
                    count -= 1
                    
                if count < 0:
                    return False
                
            return count == 0
        
        cur = []
        ans = []
        
        def bac(ind):
            if ind == 2 * n:
                res = "".join(cur)
                if check(res):
                    ans.append(res)
                    
                return
            
            cur.append("(")
            bac(ind + 1)
            cur.pop()
            cur.append(")")
            bac(ind + 1)
            cur.pop()
            
        bac(0)
        
        return ans
                    