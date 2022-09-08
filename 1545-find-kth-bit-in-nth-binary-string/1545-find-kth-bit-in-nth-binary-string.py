class Solution:
    def findKthBit(self, n: int, k: int, string = "0") -> str:
        if n == 0:
            return string[k-1]
        temp = ""
        for i in reversed(string):
            if i == "0":
                temp += "1"
            else:
                temp += "0"
        return self.findKthBit(n-1,k,string+"1"+temp)
        