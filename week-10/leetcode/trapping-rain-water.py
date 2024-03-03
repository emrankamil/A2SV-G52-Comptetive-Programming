class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_wall = defaultdict(int)
        right_wall = defaultdict(int)
        left_max = height[0]
        right_max = height[-1]

        for i in range(len(height)):
            if height[i] < left_max:
                left_wall[i] = left_max
            else:
                left_wall[i] = -1
                left_max = height[i]
            
            if height[n-i-1] < right_max:
                right_wall[n-i-1] = right_max
            else:
                right_wall[n-i-1] = -1
                right_max = height[n-i-1]
            
        rst = 0
        for i in range(len(height)):
            if right_wall[i] != -1 and left_wall[i] != -1:
                rst += min(right_wall[i], left_wall[i])-height[i]

        return rst


        # stack = [height[0]]
        # check = [1]*len(height)
        # cur_max = height[-1]

        # for i in range(len(height)-1, -1, -1):
        #     if height[i] > cur_max:
        #         check[i] = -1
        #         cur_max = height[i]
        # print(check)

        # i = 1
        # while i < len(height):
        #     while stack and height[i] >= stack[0]:
        #         x = stack.pop()
        #         if stack:
        #             rst += stack[0]-x

        #     if check[i] == -1:
        #         i += 1
        #         continue
        #     stack.append(height[i])
        #     i += 1
        # return rst