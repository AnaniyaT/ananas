class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = ["" for _ in range(len(num1)+len(num2))]
        def num(d):
            res = 0
            for i in range(len(d)):
                res += (10**i)*(ord(d[~i])-48)
            return res
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                dig1 = num1[~i]
                dig2 = num2[~j]
                result[~(i+j)] = str(num(result[~(i+j)])+(num(dig1)*num(dig2)))
        for ind in range(len(result)):
            digit = result[~ind]
            if len(digit) > 1:
                left = digit[:len(digit)-1]
                right = digit[~0]
                result[~ind] = right
                result[~(ind+1)] = str(num(result[~(ind+1)])+num(left))
            
        return str(num("".join(result)))
                
                
        