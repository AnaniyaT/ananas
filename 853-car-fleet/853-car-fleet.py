class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        dic = {}
        for ind in range(len(position)):
            dic[position[ind]] = speed[ind]
        sortedd = sorted(dic,reverse = True)
        fleets = 0
        curr = 0
        for car in sortedd:
            timeTaken = float((target-car))/float(dic[car])
            if timeTaken > curr:
                fleets += 1
                curr = timeTaken
        return fleets
                
            