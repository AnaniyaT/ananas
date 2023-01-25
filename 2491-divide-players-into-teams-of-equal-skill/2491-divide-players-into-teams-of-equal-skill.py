class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        summ = skill[-1] + skill[0]
        for ind in range(len(skill)//2):
            if skill[ind] + skill[~ind] == summ:
                chemistry += skill[ind]*skill[~ind]
            else:
                return -1
            
        return chemistry