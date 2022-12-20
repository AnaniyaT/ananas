class Solution:
    def average(self, salary: List[int]) -> float:
        maxx = 0
        minn = float('inf')
        for amount in salary:
            maxx = max(maxx, amount)
            minn = min(minn, amount)
        return (sum(salary)-(maxx+minn))/(len(salary)-2)