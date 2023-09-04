class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        curLine = []
        curLen = 0
        
        def doTheDeed(align):
            nonlocal curLen, curLine
            spaces = maxWidth - curLen
            length = len(curLine)
            if length == 1:
                length = 2
            newLine = []
            divided = spaces // (length - align)
            left = spaces % (length - align)
            for w in curLine[:length - align]:
                newLine.append(w)
                space = divided
                if left:
                    newLine.append(" " * (space + 1))
                    left -= 1
                else:
                    newLine.append(" " * space)
                
            if len(curLine) != 1 and align == 1:
                newLine.append(curLine[-1])
                
            lines.append("".join(newLine))
            curLine = []
            curLen = 0
        
        for word in words:
            if curLen + len(word) + len(curLine) > maxWidth:
                doTheDeed(1)
                
            curLine.append(word)
            curLen += len(word)
               
        newLine = []
        spaces = maxWidth - curLen
        for w in curLine[:len(curLine) - 1]:
            newLine.append(w)
            newLine.append(" ")
            spaces -= 1
        
        newLine.append(curLine[-1])
        newLine.append(" " * spaces)
        lines.append("".join(newLine))
            
        return lines