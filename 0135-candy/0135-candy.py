class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies =[1]*len(ratings)
        
        for ind in range(1, len(ratings)):
            if ratings[ind] > ratings[ind-1] and candies[ind] <= candies[ind-1]:
                candies[ind] = candies[ind-1] + 1
                
            if ratings[~ind] > ratings[~(ind-1)] and candies[~ind] <= candies[~(ind-1)]:
                candies[~ind] = candies[~(ind-1)] + 1
                
        return sum(candies)
            