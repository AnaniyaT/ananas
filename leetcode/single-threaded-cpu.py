class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        sortedd = sorted([ind for ind in range(n)], key=lambda x: tasks[x][0])
        
        time = tasks[sortedd[0]][0]
        i = 0
        
        queue = []
        
        while i < n and tasks[sortedd[i]][0] <= time:
            task = tasks[sortedd[i]]
            heappush(queue, (task[1], sortedd[i]))
            i += 1
        
        ans = []
        
        while queue:
            cur = heappop(queue)
            task = tasks[cur[1]]
            
            ans.append(cur[1])
            time += task[1]
            if not queue and i < n and time < tasks[sortedd[i]][0]:
                time = tasks[sortedd[i]][0]
                
            while i < n and (tasks[sortedd[i]][0] <= time):
                task = tasks[sortedd[i]]
                heappush(queue, (task[1], sortedd[i]))
                i += 1
            
            
        return ans
            
            
        