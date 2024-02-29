class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Dictionary to store words grouped by their lengths
        lens_to_str = defaultdict(list)
        
        # Group words by their lengths
        for word in words:
            lens_to_str[len(word)].append(word)

        # Function to check if one word is a predecessor of another
        def is_pred(word, nei_word):
            diff_count = i = 0
            while i < len(word):
                if word[i] == nei_word[i + diff_count]:
                    i += 1
                else:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return True

        # Memoized DFS function to find the longest chain
        @cache
        def dfs(word):
            mx = 1
            # For each neighbor word in the next length group
            for nei_word in lens_to_str[len(word) + 1]:
                if is_pred(word, nei_word):
                    # Calculate the length of the chain recursively
                    can_be_mx = dfs(nei_word) + 1
                    # Update the maximum length if necessary
                    if mx < can_be_mx:
                        mx = can_be_mx
            return mx

        # Initialize the maximum chain length
        ans = 0
        # Iterate through the groups of words by length
        for len_to_str in list(lens_to_str.values()):
            for word in len_to_str:
                # Find the longest chain for each word
                ans = max(ans, dfs(word))

        return ans

