class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        
        queue = deque()
        step = 0
        
        if '0000' in visited:
            return -1
        
        visited.add('0000')
        queue.append('0000')
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop()
                if cur == target:
                    return step
                
                cur = list(cur)
                for ind in range(4):
                    prev = cur[ind]
                    cur[ind] = str((int(prev) + 1) % 10)
                    joined = ''.join(cur)
                    if joined not in visited:
                        visited.add(joined)
                        queue.appendleft(joined)
                    cur[ind] = str((int(prev) - 1) % 10)
                    joined = ''.join(cur)
                    if joined not in visited:
                        visited.add(joined)
                        queue.appendleft(joined)
                    cur[ind] = prev
            # print(queue)
            step += 1
            
        return -1
                    
        
        
        