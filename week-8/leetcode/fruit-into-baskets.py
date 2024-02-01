class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        rst = 0
        left = 0
        container = defaultdict(int)
        for i in range(len(fruits)):
            container[fruits[i]] = i
            if len(container) == 3:
                for num in container:
                    if num!=fruits[i] and num!=fruits[i-1]:
                        left = container[num]+1
                        del container[num]
                        break
            rst = max(rst, i-left+1)
        return rst