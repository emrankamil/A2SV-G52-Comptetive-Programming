class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        rst = []
        col, diagonal1, diagonal2 =  set(), set(), set()

        def searchPosition(queens, cur_row):
            if queens == n:
                cur = deepcopy(board)
                rst.append(cur)
            
            for j in range(n):
                if j not in col and j-cur_row not in diagonal1 and j+cur_row not in diagonal2:
                    board[cur_row][j] = 'Q'
                    queens += 1
                    col.add(j)
                    diagonal1.add(j-cur_row)
                    diagonal2.add(j+cur_row)

                    searchPosition(queens, cur_row+1)

                    board[cur_row][j] = "."
                    queens -= 1
                    col.remove(j)
                    diagonal1.remove(j-cur_row)
                    diagonal2.remove(j+cur_row)

        searchPosition(0, 0)
        for comb in rst:
            for i in range(len(comb)):
                comb[i] = "".join(comb[i])
        return rst