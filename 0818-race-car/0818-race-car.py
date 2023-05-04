class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        
        level = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                pos, vel = queue.pop()
                if pos == target:
                    return level
                
                A = (pos + vel, 2 * vel)
                R = (pos, -(vel//abs(vel)))
                
                if A not in visited:
                    queue.appendleft(A)
                    visited.add(A)
                
                if R not in visited:
                    queue.appendleft(R)
                    visited.add(R)
                
                
            level += 1
            
        