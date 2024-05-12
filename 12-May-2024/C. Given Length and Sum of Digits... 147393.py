# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

def solve():
    m, s = map(int, input().split())
    minn, maxx = "", ""
    min_sum, max_sum = s, s

    def is_possible(m, s):
        return s >= 0 and s <= 9 * m

    for i in range(m):
        min_val, max_val = 10, -1
        for j in range(10):
            if (i > 0 or j > 0 or (m == 1 and j == 0)) and is_possible(m - i - 1, min_sum - j):
                min_val = min(min_val, j)
            if (i > 0 or j > 0 or (m == 1 and j == 0)) and is_possible(m - i - 1, max_sum - j):
                max_val = max(max_val, j)
        if min_val == 10: return '-1 -1'
        if max_val == -1: return '-1 -1'

        minn += str(min_val)
        maxx += str(max_val)

        min_sum -= min_val
        max_sum -= max_val
    return minn + ' ' + maxx

   

print(solve())