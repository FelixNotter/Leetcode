"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(emp):

            res = emp.importance
            for worker in employees:
                for subordinate in emp.subordinates:
                    if worker.id == subordinate:
                        res+=dfs(worker)
            return res




        for employee in employees:
            if employee.id == id:
                return dfs(employee)
        