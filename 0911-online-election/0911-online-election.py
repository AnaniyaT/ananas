class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        voteCount = defaultdict(int)
        
        voteCount[persons[0]] += 1
        
        self.times = times
        self.topVoted = [persons[0]]
        
        for ind in range(1, len(persons)):
            person = persons[ind]
            prev = self.topVoted[-1]
            voteCount[person] += 1
            
            if voteCount[prev] > voteCount[person]:
                self.topVoted.append(prev)
            else:
                self.topVoted.append(person)
                
        print("topVoted", self.topVoted)

    def q(self, t: int) -> int:
        ind = bisect_right(self.times, t) - 1
        
        return self.topVoted[ind]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)