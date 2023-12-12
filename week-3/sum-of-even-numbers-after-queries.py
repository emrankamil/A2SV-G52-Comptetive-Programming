class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        rst = [0]*len(queries)
        for num in nums:
            if num%2 == 0:
                evenSum += num
        for i,query in enumerate(queries):
            if (nums[query[1]]+query[0])%2 == 0:
                evenSum += query[0]
                if query[0]%2 == 1:
                    evenSum += nums[query[1]]
            elif nums[query[1]] % 2 ==0:
                evenSum -= nums[query[1]]

            rst[i] = evenSum
            nums[query[1]] += query[0]
        return rst
        
            