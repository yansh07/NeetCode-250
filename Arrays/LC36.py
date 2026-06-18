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
    
# The Approach: Hash Sets trackingThe most efficient way to solve this is to iterate through every cell in the 9 times 9 grid exactly once. 
# As we traverse, we keep track of the numbers we have already seen using Hash Sets (or arrays).
# We create three collections of sets:rows: An array of 9 sets, where rows[r] stores digits seen in row r.cols: 
# An array of 9 sets, where cols[c] stores digits seen in column $c$.boxes: An array of 9 sets, where boxes[box_idx] stores digits seen in the 3  times 3 sub-box.
