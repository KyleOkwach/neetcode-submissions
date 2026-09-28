class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif (
                    board[row][col] in rows[row] or  # check if value is in current row
                    board[row][col] in cols[col] or  # check if value is in current column
                    board[row][col] in squares[row // 3, col // 3]  # check if value is in current 3x3 square
                ):
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        return True
        