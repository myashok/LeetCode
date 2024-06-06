class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        graph = defaultdict(list)
        n = len(beginWord)
        for word in word_set:
            if len(word) != n:
                continue
            for i in range(n):
                pattern = word[:i] + '*' + word[i+1:]
                graph[pattern].append(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while queue:
            current_word, dist = queue.popleft()
            if current_word == endWord:
                return dist
            for i in range(n):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for next_word in graph[pattern]:
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, dist + 1))
        return 0


