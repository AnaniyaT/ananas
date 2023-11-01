class UndergroundSystem:

    def __init__(self):
        self.people = {}
        self.travelTimes = defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.people[id]
        self.travelTimes[(startStation, stationName)][0] += t - startTime
        self.travelTimes[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.travelTimes[(startStation, endStation)]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)