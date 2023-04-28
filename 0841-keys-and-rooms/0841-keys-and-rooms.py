class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])
        
        while queue:
            curr = queue.pop()
            
            for key in rooms[curr]:
                if key not in visited:
                    visited.add(key)
                    queue.appendleft(key)
                    
        return len(visited) == len(rooms)