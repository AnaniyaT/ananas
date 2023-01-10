class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        sequentialNums = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(digits[start:start+length])
                if num >= low and num <= high:
                    sequentialNums.append(num)
                    
        return sequentialNums
                    