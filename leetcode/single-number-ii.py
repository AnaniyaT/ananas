class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0 for _ in range(33)]
        
        for num in nums:
            binary = bin(num)
            ex = 2
            if binary[0] == "-":
                ex = 3
                bits[32] += 1
                
            for ind, bit in enumerate(reversed(binary[ex:])):
                if bit == '1':
                    bits[ind] += 1
                    
        num = 0
        for ind in range(32):
            if bits[ind] % 3:
                num += 2 ** ind
                
        if bits[32] % 3:
            num *= -1
        
        # print(bits)
        # print(bin(-2147483648))
        return num
        
       