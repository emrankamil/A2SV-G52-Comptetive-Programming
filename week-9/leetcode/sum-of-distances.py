class Solution:
    
    def distance(self, nums: List[int]) -> List[int]:
        counter = defaultdict(list)
        for i,num in enumerate(nums):
            counter[num].append(i)
        rst = [0]*len(nums)

        def solver(arr):
            total = sum(arr)-arr[0]*(len(arr))
            rst[arr[0]] = total
            for i in range(1,len(arr)):
                total += (arr[i]-arr[i-1])*(i)
                total -= (arr[i]-arr[i-1])*(len(arr)-(i))
                rst[arr[i]] = total

        for num in counter:
            if len(counter[num]) == 1:
                rst[counter[num][0]] = 0
            else:
                solver(counter[num])

        return rst

        
        