class Solution:
    def abs(self, num):
        if num < 0:
            return 0 - num
        return num
    
    def divide(self, dividend: int, divisor: int) -> int:
        if self.abs(divisor) > self.abs(dividend) or not dividend:
            return 0
        
        sign = 1
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            sign = -1
            
        dividend = self.abs(dividend)
        divisor = self.abs(divisor)
            
        twos = [1]
        multiples = [divisor]
        cur = 1
        
        while multiples[-1] < dividend:
            cur += cur
            twos.append(cur)
            multiples.append(multiples[-1] + multiples[-1])
            
        # print(twos)
        # print(multiples)
        
        p = len(twos) - 2
        last = multiples[-1]
        while not(0 <= dividend - last < divisor):
            # print(p)
            if last > dividend:
                cur -= twos[p]
                last -= multiples[p]
            else:
                cur += twos[p]
                last += multiples[p]
                
            p -= 1
            
        if sign == -1:
            return max(0 - cur, -2**31)
        
        return min(cur, 2**31 - 1)
            