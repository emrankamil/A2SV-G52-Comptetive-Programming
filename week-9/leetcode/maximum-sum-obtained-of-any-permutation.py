class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        total_req = [0]*n
        for start, end in requests:
            total_req[start] += 1
            if end < n-1:
                total_req[end+1] -= 1
        for i in range(1,n):
            total_req[i] += total_req[i-1]

        total_req.sort(reverse=True)
        nums.sort(reverse=True)
        

        rst = 0
        for i in range(n):
            if not total_req[i]:
                break
            rst += total_req[i]*nums[i]
            
        return rst%(10**9 + 7)
