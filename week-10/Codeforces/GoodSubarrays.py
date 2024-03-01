t = int(input())

for _ in range(t):
    n = int(input())
    nums = input()
    prefix = {0:1}
    cummulative = 0
    rst = 0
    for i, val in enumerate(nums):
        cummulative += int(val)
        diff = cummulative-i-1
        if diff in prefix:
            rst += prefix[diff]
            prefix[diff] += 1
        else:
            prefix[diff] = 1
    print(rst)