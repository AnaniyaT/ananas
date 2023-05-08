class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for ind in range(len(recipes)):
            for fro in ingredients[ind]:
                graph[fro].append(recipes[ind])
                indegree[recipes[ind]] += 1
        
        recipes = set(recipes)
        canMake = []
        queue = deque(supplies)
        
        while queue:
            cur = queue.pop()
            if cur in recipes:
                canMake.append(cur)
            
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                
                if not indegree[neigh]:
                    queue.appendleft(neigh)
                    
        return canMake