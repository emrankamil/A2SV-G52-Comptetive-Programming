class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        rst = 0
        j = 0 
        for i in range(0, len(tasks),4):
            rst = max(rst, tasks[i]+processorTime[i//4])
        return rst