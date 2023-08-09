class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        maximum = [0 for _ in range(len(questions))]
        
        def getMax(ind):
            if ind >= len(maximum):
                return 0
            return maximum[ind]
        
        curMax = 0
        for ind in range(len(questions)-1, -1, -1):
            power, skip = questions[ind]
            maximum[ind] = max(power + getMax(ind + skip + 1), getMax(ind + 1))
        
        return max(maximum)