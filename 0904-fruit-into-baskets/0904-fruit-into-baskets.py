class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            
            if len(basket) > 2:
                basket[fruits[l]] -= 1
                if not basket[fruits[l]]:
                    basket.pop(fruits[l])
                    
                l += 1
                
        return len(fruits)-l
        