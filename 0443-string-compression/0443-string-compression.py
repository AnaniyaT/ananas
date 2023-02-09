class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        prev = ""
        count = 0
        
        for char in chars:
            if char == prev:
                count += 1
            else:
                if count:
                    for d in str(count+1):
                        chars[l] = d
                        l += 1
                    count = 0
                    
                chars[l] = char
                l += 1
                prev = char
                
        if count:
            for d in str(count+1):
                chars[l] = d
                l += 1
            
        return l
                
                    
                