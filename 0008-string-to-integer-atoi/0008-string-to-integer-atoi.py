class Solution(object):
    def myAtoi(self, s):
        if not s: return 0
        res, sign = "0", 1
        for i in range(len(s)):
            if s[i] != " ":
                if s[i] == "-":
                    sign = -1
                    i += 1
                elif s[i] == "+":
                    i += 1
                break
        for j in range(i, len(s)):
            if s[j].isdigit():
                res += s[j]
            else:
                break
        num = sign*int(res)
        if num < -2**31: num = -2**31
        if num > 2**31 - 1: num = 2**31 - 1
        return num
        