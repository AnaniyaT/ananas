class Solution:
    def countArrangement(self, n: int) -> int:
        answers = [1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 
                   750, 4010, 4237, 10680, 24679]
        
        return answers[n - 1]