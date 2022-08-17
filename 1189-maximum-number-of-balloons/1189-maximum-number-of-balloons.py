class Solution(object):
    def maxNumberOfBalloons(self, text):
        mylistt = [0,0,0,0,0]
        for char in text:
            if char == "b":
                mylistt[0] += 1
            elif char == "a":
                mylistt[1] += 1
            elif char == "l":
                mylistt[2] += 0.5
            elif char == "o":
                mylistt[3] += 0.5
            elif char == "n":
                mylistt[4] += 1
        return int(min(mylistt))
            
        