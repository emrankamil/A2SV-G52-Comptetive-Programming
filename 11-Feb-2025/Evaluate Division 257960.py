# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            num, den = equations[i]
            graph[num].append([den, values[i]])
            graph[den].append([num, 1/values[i]])
        
        def dfs(start, dest, cur):
            for denom, value in graph[start]:
                if denom == dest:
                    return cur*value
                if denom not in visited:
                    visited.add(denom)
                    result = dfs(denom, dest, cur*value)
                    if result:
                        return result
        
        result = []
        for a, b in queries:
            visited = set([])
            mult = dfs(a, b, 1)
            if mult:
                result.append(mult)
            else:
                result.append(-1)

        return result