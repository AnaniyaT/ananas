class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        f, s, n = "IPv4", "IPv6", "Neither"
        lett = 'abcdef'
        hexLetters = lett + lett.upper()
        
        if "." in queryIP:
            splitt = queryIP.split(".")
            if len(splitt) != 4:
                return n
            
            for chunk in splitt:
                if not chunk.isdigit() or (chunk[0] == "0" and len(chunk) > 1):
                    return n
                
                if int(chunk) > 255 or int(chunk) < 0:
                    return n
                
            return f
        
        if ":" in queryIP:
            splitt = queryIP.split(":")
            if len(splitt) != 8:
                return n
            
            for chunk in splitt:
                if len(chunk) > 4 or len(chunk) < 1:
                    return n
                
                for c in chunk:
                    if not c.isdigit() and c not in hexLetters:
                        return n
                    
            return s
            
        return n