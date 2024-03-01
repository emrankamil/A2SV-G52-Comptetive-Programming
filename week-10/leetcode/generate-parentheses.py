class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rst = []
        def backtrack(cur, count_left, count_right):
            if len(cur) == 2*n:
                rst.append("".join(cur[:]))

            for i in ['(',')']:
                if i==')':
                    if count_right<count_left:
                        count_right += 1
                        cur.append(i)
                        backtrack(cur, count_left, count_right)
                        cur.pop()
                        count_right -= 1
                elif i == '(' and count_left<n:
                    count_left += 1
                    cur.append(i)
                    backtrack(cur, count_left, count_right)
                    cur.pop()
                    count_left -= 1
                
        backtrack([], 0, 0)
        return rst