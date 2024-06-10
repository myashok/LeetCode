class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        m = len(board)
        n = len(board[0])
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        direction = [(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, -1), (1, 1), (0, 1), (0, -1)]
        def get_adjacent(x, y):
            adj = []
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    adj.append((nx, ny))
            return adj


        def dfs(r, c):
            adj = get_adjacent(r, c)
            mines = sum(board[nr][nc] == 'M' for nr, nc in adj)
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for nr, nc in adj:
                    if board[nr][nc] == 'E':
                        dfs(nr, nc)
        dfs(r, c)
        return board

