class Solution:
    def __init__(self):
        self.ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.twos = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 
                     'Seventeen', 'Eighteen', 'Nineteen']
        self.tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.suffixes = ['Thousand', 'Million', 'Billion']
    
    def numberToWords(self, num: int) -> str:
        sNum = str(num)
        if len(sNum) == 1:
            return self.ones[num]
        if len(sNum) == 2:
            if sNum[0] == "1":
                return self.twos[int(sNum[1])]
            else:
                first = self.tens[int(sNum[0])-2]
                last = " " + self.ones[int(sNum[1])] if int(sNum[1]) != 0 else ""
                return f"{first}{last}"
        if len(sNum) == 3:
            first = self.ones[int(sNum[0])]
            last = " " + self.numberToWords(int(sNum[1:])) if int(sNum[1:]) != 0 else ""
            return f"{first} Hundred{last}"
        
        suffix = self.suffixes[((len(sNum)-1)//3)-1] 
        rang = 3 if not len(sNum)%3 else len(sNum)%3
        first = self.numberToWords(int(sNum[:rang])) + " " if sNum[:rang] else ""
        last = " " + self.numberToWords(int(sNum[rang:])) if int(sNum[rang:]) != 0 else ""
        
        return f"{first}{suffix}{last}"
        
        