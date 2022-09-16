class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        boats, l, r = 0, 0, len(people) -1
        while l <= r:
            if not people[l]+people[r] > limit:
                l += 1 
            boats += 1
            r -= 1
        return boats

            