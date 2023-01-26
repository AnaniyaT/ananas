class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        summ = 0
        piles.sort(reverse=True)
        for ind in range(len(piles)//3):
            summ += piles[ind*2 + 1]
            
        return summ
