class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class TrieNode():
            def __init__(self):
                self.children = {}
                self.is_end = False
        
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str) -> None:
                node = self.root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end = True

            def search(self, word: str) -> bool:
                node = self.root
                for char in word:
                    if char not in node.children:
                        return False
                    node = node.children[char]
                    if node.is_end:
                        return True
                return False

        folder.sort()
        ans = []
        trie = Trie()
        for folder in folder:
            words = folder.split('/')
            if not trie.search(words):
                trie.insert(words)
                ans.append("/".join(words))
        return ans
