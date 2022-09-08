class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        string = "0"
        for i in range (n-1):
            temp = ""
            for bit in reversed(string):
                temp += "0" if bit == "1" else "1"
            string += "1"+temp
        return string[k-1]