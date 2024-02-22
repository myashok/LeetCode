class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        rows = len(board)
        cols = len(board[0])
        def solve(r, c, i):
            if board[r][c] != word[i]:
                return False
            if i == word_len-1:
                return True
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            board_val, board[r][c] = board[r][c], '*'
            for dx, dy in direction:
                new_r = r + dx
                new_c = c + dy
                if 0 <= new_r < rows and 0 <= new_c < cols and solve(new_r, new_c, i + 1):
                    return True
            board[r][c] = board_val
            return False
        for i in range(rows):
            for j in range(cols):
                    if solve(i, j, 0):
                        return True
        return False

                
