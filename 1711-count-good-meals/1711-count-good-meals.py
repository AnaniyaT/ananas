class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = {}
        goodMeal = 0
        for food in deliciousness:
            for p in range(22):
                target = (2**p) - food
                if target in counter:
                    goodMeal += counter[target]
            if food in counter:
                counter[food] += 1
            else:
                counter[food] = 1
        return goodMeal%((10**9)+7)
        