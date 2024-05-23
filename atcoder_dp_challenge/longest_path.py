from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

# top-down
memo = {}
def dp(i):
    if i > n:
        return -1
    if i not in memo:
        next_longest  = 0
        for neigh in graph[i]:
            next_longest = max(next_longest, dp(neigh) + 1)
        memo[i] = next_longest
    return memo[i]

# longest = 0
# for i in range(1, n + 1):
#     longest = max(longest, dp(i))
# print(longest)

# bottom up

dp = [-1] * (n + 1)
def dfs(i):
    cur_longest = 0
    if dp[i] == -1:
        for neigh in graph[i]:
            cur_longest = max(cur_longest, dfs(neigh) + 1)
        dp[i] = cur_longest
    return dp[i]

def main():
    longest = 0
    for i in range(1, n + 1):
        longest = max(longest, dfs(i))
    print(longest)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
