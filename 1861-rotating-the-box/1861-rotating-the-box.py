class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        
        ans = [["."] * n for _ in range(m)]
        
        for r in range(n):
            cnt = 0
            for c in range(m):
                if box[r][c] == "#":
                    cnt += 1
                elif box[r][c] == "*":
                    ans[c][~r] = "*"
                    for col in range(c-1, c-cnt-1, -1):
                        ans[col][~r] = "#"
                    cnt = 0
                    
            for col in range(m-1, m-cnt-1, -1):
                ans[col][~r] = "#"
                
        return ans