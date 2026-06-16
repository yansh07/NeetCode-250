# Valid Sudoku

class Solution:
    def isValidSudoku(self, board: list[list[int]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # skip empty cell
                if val == ".":
                    continue

                # calc current 3*3 box index 
                box_idx = (r // 3) * 3 + (c // 3)

                # check for duplicate in row, col, and box 
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # add the current val to representative set 
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
            
        return True