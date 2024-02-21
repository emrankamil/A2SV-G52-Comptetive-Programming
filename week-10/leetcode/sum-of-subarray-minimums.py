class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        #calculate the next smaller element
        track1 = defaultdict(int)
        stack = []
        for i in range(len(arr)):
            while stack and arr[i]<=arr[stack[-1]]:
                track1[stack.pop()] = i
            stack.append(i)
        for i in stack:
            track1[i] = len(arr)

        # calculate the previous smaller element
        stack2 = []
        track2 = defaultdict(int)
        for i in range(len(arr)-1,-1,-1):
            while stack2 and arr[i]<arr[stack2[-1]]:
                track2[stack2.pop()] = i
            stack2.append(i)
        for i in stack2:
            track2[i] = -1

        rst = 0
        for i in range(len(arr)):
            rst += (track1[i]-i)*(i-track2[i])*arr[i]
        return rst%(10**9 + 7)
