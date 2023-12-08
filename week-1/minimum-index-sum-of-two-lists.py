class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}  # Store indices of elements from list1
        
        for i, item in enumerate(list1):
            index_map[item] = i
        
        result = []
        min_sum = float('inf')
        
        for j, item in enumerate(list2):
            if item in index_map:
                total_sum = index_map[item] + j
                if total_sum < min_sum:
                    result = [item]
                    min_sum = total_sum
                elif total_sum == min_sum:
                    result.append(item)
        
        return result
