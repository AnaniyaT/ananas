class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        # (a + bi)(c + di) = ac - bd + (ad + cb)i
        
        # Get a, b, c and d
        num1Split = num1.split("+")
        num2Split = num2.split("+")
        a = int(num1Split[0])
        b = int(num1Split[1][:-1])
        c = int(num2Split[0])
        d = int(num2Split[1][:-1])
        
        product = f"{a*c - b*d}+{a*d + c*b}i"
        
        return product
        
        