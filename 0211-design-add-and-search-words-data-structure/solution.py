class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the
        dot character '.' to represent any one letter.
        """
        def _search(node, word):
            for i, char in enumerate(word):
                if char == '.':
                    # If the character is '.', check all possible children nodes
                    for child in node.children.values():
                        if _search(child, word[i+1:]):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.end
        
        return _search(self.trie, word)

# Example usage:
# obj = WordDictionary()
# obj.addWord("bad")
# print(obj.search("b.d"))  # Should return True
# print(obj.search("b.."))  # Should return True
# print(obj.search("bad"))  # Should return True
# print(obj.search("ba"))   # Should return False

