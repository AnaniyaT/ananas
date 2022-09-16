class Solution:
    def compress(self, chars: List[str]) -> int:
        indx = 0
        curr = ""
        count = 1
        for i in chars:
            if i == curr:
                count += 1   
            else:
                curr = i
                if count > 1:
                    for i in str(count):
                        chars[indx] = i
                        indx += 1
                chars[indx] = curr
                indx += 1
                count = 1
        if count > 1:
            for i in str(count):
                chars[indx] = i
                indx += 1
        return indx