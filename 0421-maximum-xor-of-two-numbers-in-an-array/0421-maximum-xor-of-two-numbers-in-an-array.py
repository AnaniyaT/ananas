class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        node = [None, None]
        root = node[:]
        maxXor = 0
        
        def binary(num):
            b = list(map(int, bin(num)[2:]))
            return ([0] * (32 - len(b))) + b
        
        def maXor(num):
            binry = binary(num)
            cur = root
            xor = 0
            p = 31
            
            for b in binry:
                if cur[1-b]:
                    cur = cur[1-b]
                    xor += 2 ** p
                else:
                    if not cur[b]:
                        return xor
                    cur = cur[b]
                p -= 1
                
            return xor
        
        def insert(num):
            nonlocal maxXor
            
            maxXor = max(maxXor, maXor(num))
            
            binry = binary(num)
            cur = root
            
            for b in binry:
                if not cur[b]:
                    cur[b] = node[:]
                
                cur = cur[b]
        
        for num in nums:
            insert(num)
            
        return maxXor
        
                    