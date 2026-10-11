class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def capture(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS -1] or c in [0, COLS - 1])):
                    capture(r,c)
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
            

        # ROWS, COLS = len(board), len(board[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # def capture():
        #     q = deque()
        #     for r in range(ROWS):
        #         for c in range(COLS):
        #             if (r == 0 or r == ROWS - 1 or
        #                 c == 0 or c == COLS - 1) and board[r][c] == "O":
        #                 q.append((r, c))
        #     while q:
        #         r, c = q.popleft()
        #         if board[r][c] == "O":
        #             board[r][c] = "T"
        #             for dr, dc in directions:
        #                 nr, nc = r + dr, c + dc
        #                 if 0 <= nr < ROWS and 0 <= nc < COLS:
        #                     q.append((nr, nc))

        # capture()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] == "O":
        #             board[r][c] = "X"
        #         elif board[r][c] == "T":
        #             board[r][c] = "O"