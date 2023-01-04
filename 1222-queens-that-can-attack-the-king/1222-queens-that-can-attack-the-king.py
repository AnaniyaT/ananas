class Solution:      
    
    #function to look for attacking queens and append them to an array answer
    def look(self, startY, startX, down, right, distance, answer, queensSet):
        for _ in range(distance):
            startY += down
            startX += right
            if tuple([startX, startY]) in queensSet:
                answer.append([startX, startY])
                break
        
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queensSet = set(map(tuple, queens))
        answer = []
        startY = king[1]
        startX = king[0]
        
        #Search queens to the right
        distance = 7 - king[0]
        down = 0
        right = 1
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        #Search queens to the left
        distance = king[0]
        down = 0
        right = -1
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        #Search queens to the top
        distance = king[1]
        down = -1
        right = 0
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        #Search queens to the bottom
        distance = 7 - king[1]
        down = 1
        right = -0
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        #Search queens to the top left
        distance = min(king[0], king[1])
        down = -1
        right = -1
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        #Search queens to the top right
        distance = min(7 - king[0], king[1])
        down = -1
        right = 1
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        #Search queens to the bottom left
        distance = min(7 - king[1], king[0])
        down = 1
        right = -1
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        #Search queens to the bottom right
        distance = min(7 - king[1], 7 - king[0])
        down = 1
        right = 1
        self.look(startY, startX, down, right, distance, answer, queensSet)
        
        return answer
        
        