class Solution:
    @cache
    def finalScore(self,score, nums, l, r, isP1):
        if isP1 and l == r:
            return (score[0]+nums[l], score[1])
        
        if not isP1 and l == r:
            return (score[0], score[1]+nums[l])
        
        p1Score = score[0]
        p2Score = score[1]
        
        if isP1:
            leftScore = (p1Score + nums[l], p2Score)
            rightScore = (p1Score + nums[r], p2Score)
            
            left = self.finalScore(leftScore, nums, l+1, r, not isP1)
            right = self.finalScore(rightScore, nums,l, r-1, not isP1)
            
            return max([left, right], key=lambda x: x[0]-x[1])
        
        else:
            leftScore = (p1Score , p2Score + nums[l])
            rightScore = (p1Score , p2Score + nums[r])
            
            left = self.finalScore(leftScore, nums, l+1, r, not isP1)
            right = self.finalScore(rightScore, nums,l, r-1, not isP1)
            
            return max([left, right], key=lambda x: x[1]-x[0])
            
            
    def PredictTheWinner(self, nums: List[int]) -> bool:
        finalScore = self.finalScore((0, 0), tuple(nums), 0, len(nums)-1, True)
        p1Score = finalScore[0]
        p2Score = finalScore[1]
        
        return p1Score >= p2Score
        