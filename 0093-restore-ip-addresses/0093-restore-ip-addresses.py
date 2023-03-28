class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valids = []
        curr = []
        
        def backtrack(strng, d):
            if not d:
                if int(strng) <= 255 and len(strng) == len(str(int(strng))):
                    address = ".".join(curr) + f".{str(int(strng))}"
                    valids.append(address)
                return
            
            for ind in range(1, len(strng)):
                num = strng[:ind]
                if int(num) <= 255 and len(num) == len(str(int(num))):
                    curr.append(str(num))
                    backtrack(strng[ind:], d - 1)
                    curr.pop()
                    
                    
        backtrack(s, 3)
        
        return list(set(valids))