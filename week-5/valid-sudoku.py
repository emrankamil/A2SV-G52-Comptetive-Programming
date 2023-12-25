class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if len(set(row))+row.count(".") != 10:
                return False
        
        for i in range(9):
            checkSet = set()
            for j in range(9):
                if board[j][i].isalnum() and board[j][i] in checkSet:
                    return False
                else:
                    checkSet.add(board[j][i])
        
        for start in ((0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)):
            checkSet = set()
            for i in range(start[0], start[0]+3):
                for j in range(start[1], start[1]+3):
                    if board[i][j].isalnum() and board[i][j] in checkSet:
                        return False
                    else:
                        checkSet.add(board[i][j])
        return True