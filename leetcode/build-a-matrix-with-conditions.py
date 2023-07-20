class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        indxes = [[-1, -1] for _ in range(k)]
        
        for ind, condition in enumerate([rowConditions, colConditions]):
            graph = [[] for _ in range(k)]
            indeg = [0 for _ in range(k)]
            
            for fro, to in condition:
                graph[fro-1].append(to-1)
                indeg[to-1] += 1
                
            queue = deque()
            visited = 0
            
            for indx in range(k):
                if not indeg[indx]:
                    queue.append(indx)
                    visited += 1
                    
            current = 0
            while queue:
                cur = queue.pop()
                indxes[cur][ind] = current
                current += 1
                
                for neigh in graph[cur]:
                    indeg[neigh] -= 1
                    if not indeg[neigh]:
                        queue.appendleft(neigh)
                        visited += 1
            
            if visited < k:
                return []
                    
        mat = [[0 for _ in range(k)] for _ in range(k)]
        
        for ind in range(k):
            r, c = indxes[ind]
            mat[r][c] = ind + 1
            
        return mat
                        
        