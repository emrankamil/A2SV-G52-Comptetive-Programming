class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = defaultdict(int)
        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)
        for num in stack:
            nextGreater[num] = -1
        for i, num in enumerate(nums1):
            nums1[i] = nextGreater[num]
        return nums1