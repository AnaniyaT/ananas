class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def backtrack(path, start, lvl):
            nonlocal k, n
            
            if not lvl:
                answer.append(path)
                return

            for num in range(start + 1, n + 1):
                backtrack(path + [num], num, lvl-1)
                
        backtrack([], 0, k)
                
        return answer