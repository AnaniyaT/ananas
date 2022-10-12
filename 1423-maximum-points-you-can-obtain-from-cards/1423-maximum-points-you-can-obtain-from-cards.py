class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = minn = summ = totSum = 0
        r = len(cardPoints) - k
        for i in range(r):
            summ += cardPoints[i]
        minn = totSum =  summ
        for p in range(r, len(cardPoints)):
            summ -= cardPoints[l]
            summ += cardPoints[p]
            totSum += cardPoints[p]
            l += 1
            minn = min(minn, summ)
            
        return totSum - minn