class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        g = [0 for _ in range(n)]
        s = [0 for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    g[i] += 1
                elif rating[j] < rating[i]:
                    s[i] += 1
        
        teams = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    teams += g[j]
                elif rating[j] < rating[i]:
                    teams += s[j]
                    
                    
        return teams
                    