class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = min(salary)
        maximum = max(salary)
        total = 0
        for s in salary:
            if s == minimum or s == maximum:
                continue
            total +=s
        return total/(len(salary)-2)
