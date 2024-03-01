class Solution:
    def totalNQueens(self, n: int) -> int:
        rst = 0
        col, diagonal1, diagonal2 =  set(), set(), set()

        def searchPosition(queens, cur_row):
            nonlocal rst
            if queens == n:
                rst += 1
            
            for j in range(n):
                if j not in col and j-cur_row not in diagonal1 and j+cur_row not in diagonal2:
                    queens += 1
                    col.add(j)
                    diagonal1.add(j-cur_row)
                    diagonal2.add(j+cur_row)

                    searchPosition(queens, cur_row+1)

                    queens -= 1
                    col.remove(j)
                    diagonal1.remove(j-cur_row)
                    diagonal2.remove(j+cur_row)

        searchPosition(0, 0)
        return rst