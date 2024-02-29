class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        single_row_combos = []
        def get_single_row_combos(bricks_used, curr_width):
            if curr_width > width:
                return

            if curr_width == width:
                single_row_combos.append(tuple(bricks_used))
                return

            for brick in bricks:
                get_single_row_combos([brick] + bricks_used, curr_width + brick)
        get_single_row_combos([], 0)
        
        combos_to_joins = defaultdict(set)
        for combos in single_row_combos:
            curr_brick_width = 0
            for brick in combos[:-1]:
                curr_brick_width += brick
                combos_to_joins[combos].add(curr_brick_width)
        
        graph_combos_to_possible_combos = defaultdict(list)
        for single_row_combo in single_row_combos:
            for nei_row_combo in single_row_combos:
                if not len(
                    combos_to_joins[single_row_combo] & combos_to_joins[nei_row_combo]
                ):
                    graph_combos_to_possible_combos[single_row_combo].append(
                        nei_row_combo
                    )
        ans = 0
        mod = 10 ** 9 +7
        
        @lru_cache(None)
        def dfs(combo, h):
            if h == height:
                return 1
            cnt = 0
            for nei_combo in graph_combos_to_possible_combos[combo]:
                cnt += dfs(nei_combo, h + 1)
            return cnt

        for single_row_combo in single_row_combos:
            ans += dfs(single_row_combo, 1)
        dfs.cache_clear()
        return ans%mod

