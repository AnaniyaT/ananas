class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        l = 0
        for i in fruits:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            if len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    dic.pop(fruits[l])
                l += 1
        return len(fruits) - l