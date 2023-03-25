class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        r = len(tokens) - 1
        tokens.sort()
        
        score = 0
        
        for ind, token in enumerate(tokens):
            if ind > r:
                break
                
            while power < token and score:
                power += tokens[r]
                score -= 1
                r -= 1
                
            if power >= token:
                score += 1
                power -= token
                
        return score