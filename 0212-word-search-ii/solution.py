class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        def __init__(self):
            self.root = self.TrieNode()
        
        def insert(self, word):
            node = self.root
            for c in word:
                if c in node.children:
                    node = node.children[c]
                else:
                    node.children[c] = self.TrieNode()
                    node = node.children[c]
            
            node.is_end = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.Trie()
        for word in words:
            trie.insert(word)
        
        res = set()
        m = len(board)
        n = len(board[0])
        
        def backtrack(r, c, path, node):
            if node.is_end:
                res.add(''.join(path))
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            value, board[r][c] = board[r][c], "*"
            for dx, dy in direction:
                new_r = r + dx
                new_c = c + dy
                if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] in node.children:
                    path.append(board[new_r][new_c])
                    backtrack(new_r, new_c, path, node.children[board[new_r][new_c]])
                    path.pop()
            
            board[r][c] = value

       
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    backtrack(i, j, [board[i][j]], trie.root.children[board[i][j]])
        return res
