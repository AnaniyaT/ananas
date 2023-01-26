class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        summ = 0
        piles.sort(reverse=True)
        for ind in range(0, 2*(len(piles)//3), 2):
            summ += piles[ind + 1]
            
        return summ
