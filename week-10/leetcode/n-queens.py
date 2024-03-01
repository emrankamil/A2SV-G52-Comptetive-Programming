class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        rst = []
        row, col, invalidDiagonal1, invalidDiagonal2 = [-1], set(), set(), set()

        def validate(i, j):
            if i in row or j in col or j-i in invalidDiagonal1 or j+i in invalidDiagonal2:
                return False
            return True

        def searchPosition(queens):
            if queens == n:
                cur = deepcopy(board)
                rst.append(cur)

            for i in range(row[-1]+1,n):
                for j in range(n):
                    if validate(i, j):
                        board[i][j] = 'Q'
                        queens += 1
                        row.append(i)
                        col.add(j)
                        invalidDiagonal1.add(j-i)
                        invalidDiagonal2.add(j+i)

                        searchPosition(queens)

                        board[i][j] = "."
                        queens -= 1
                        row.pop()
                        col.remove(j)
                        invalidDiagonal1.remove(j-i)
                        invalidDiagonal2.remove(j+i)

        searchPosition(0)
        for comb in rst:
            for i in range(len(comb)):
                comb[i] = "".join(comb[i])
        return rst