class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        return (sum(salary)-max_salary-min_salary)/(len(salary)-2)