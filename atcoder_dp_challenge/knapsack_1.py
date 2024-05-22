n, w = map(int, input().split())
items = []
for _ in range(n):
    items.append(list(map(int, input().split())))

# method 1: memoization ( top - down)

# memo = {}
# def dp(i, weight):
#     if i >= len(items):
#         return 0
#     if (i, weight) not in memo:
#         pick = dp(i + 1, weight + items[i][0]) + items[i][1] if weight + items[i][0] <= w else -float('inf')
#         no_pick = dp(i + 1, weight)
#         memo[(i, weight)] = max(pick, no_pick)
#     return memo[(i, weight)]

# method 2: Tabulation (bottom-up)
dpc = [0] * (w + 1)
for i in range(n - 1, -1, -1):
    for j in range(w):
        pick = dpc[j + items[i][0]] + items[i][1] if (items[i][0] +  j <= w) else -float('inf')
        no_pick = dpc[j] if i < n - 1 else -float('inf')
        dpc[j] = max(pick, no_pick)
print(max(dpc))
