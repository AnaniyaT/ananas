class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = {}
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in losers:
                winners.add(winner)
            if loser in winners:
                winners.remove(loser)
            if loser in losers:
                losers[loser] += 1
            else:
                losers[loser] = 1
        result = [[], []]
        for winner in winners:
            result[0].append(winner)
        for loser in losers:
            if losers[loser] == 1:
                result[1].append(loser)
        result[0].sort()
        result[1].sort()
        return result
                