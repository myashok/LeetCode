class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        node = trie
        for word in dictionary:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True
        def get_root(word):
            node = trie
            root_word = []
            for c in word:
                if '$' in node:
                    return ''.join(root_word)
                if c not in node:
                    return word
                root_word.append(c)
                node = node[c]
            return ''.join(root_word) if '$' in node else word 

        words = sentence.split(' ')
        ans = []
        for word in words:
            ans.append(get_root(word))

        return " ".join(ans)

        
