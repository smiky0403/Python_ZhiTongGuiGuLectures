class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_box(i:int, j:int) -> Set[int]:
            seen = set()
            r0 = 3 * (i//3)
            c0 = 3 * (j//3)
            for r in range(r0, r0 + 3):
                 for c in range(c0, c0 + 3):
                    tmp = board[r][c]
                    if tmp != ".":
                        seen.add(int(tmp))
            return set(seen)
        
        def get_row(i:int) -> Set[int]:
            seen = set()
            for x in board[i]:
                if x != ".":
                    seen.add(int(x))
            return set(seen)

        def get_col(j:int) -> Set[int]:
            seen = set()
            for b in board:
                if b[j] != ".":
                    seen.add(int(b[j]))
            return set(seen)

        def get_candidate(i:int, j:int) -> List[int]:
            if board[i][j] != ".":
                return []
            box = get_box(i, j)
            row = get_row(i)
            col = get_col(j)
            seen = box | row | col
            return [v for v in range(1, 10) if v not in seen]
        
        def fill_board():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    tmp = board[i][j]
                    if tmp != ".":
                        continue
                    vals = get_candidate(i, j)
                    for v in vals:
                        board[i][j]= str(v)
                        if fill_board():
                            return True
                        board[i][j]= "."
                    return False
            
            return True

        fill_board()


#This is a backup








        