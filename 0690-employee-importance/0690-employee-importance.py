"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Empcoloyee'], id: int) -> int:
        visited = set()
        importance = 0
        employeeId = {}
        for employee in employees:
            employeeId[employee.id] = employee
        
        def dfs(employee):
            nonlocal importance
            
            importance += employee.importance
            visited.add(employee)
            for _id in employee.subordinates:
                subordinate = employeeId[_id]
                if subordinate not in visited:
                    dfs(subordinate)
                    
        for emp in employees:
            if emp.id == id:
                dfs(emp)
                break
                
        return importance