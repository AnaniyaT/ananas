class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0, 0]
        
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if not change[0]:
                    return False
                change[0] -= 1
                change[1] += 1
            else:
                if change[1]:
                    change[1] -= 1
                    bill -= 10
                
                if change[0] < (bill - 5) / 5:
                    return False
                
                change[0] -= (bill - 5) / 5
                
        return True
                