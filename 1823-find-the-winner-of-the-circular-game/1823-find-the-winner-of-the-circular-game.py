class Solution:
    def findTheWinner(self, n: int, k: int, s = 0) -> int:
        players = [i for i in range(1, n+1)]
        ind = -1
        while len(players) > 1:
            ind = (ind+k)%len(players)
            players.pop(ind)
            ind -= 1
        
        return players[0]
        
        