from functools import reduce
import operator
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        g = defaultdict(list)
        n = len(cost)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            
        ans = [1]*n
        
        def get_max_mul(min_heap, max_heap):
            nums = [num for num, _ in min_heap]
            min_heap_index = set([i for _, i in min_heap])
            nums = nums + [-num for num, i in max_heap if i not in min_heap_index]
            max_mul = 0
            for i in range(len(nums)-2):
                for j in range(i+1, len(nums)-1):
                    for k in range(j+1, len(nums)):
                        max_mul = max(max_mul, nums[i]*nums[j]*nums[k])
            return max_mul

        def dfs(u, p):
            cnt = 0
            max_heap = []
            min_heap = []
            for v in g[u]:
                if v != p:
                    v_max_heap, v_min_heap = dfs(v, u)
                    for (min_ele, i_min), (max_ele, i_max)  in zip(v_min_heap, v_max_heap):
                        if len(max_heap) == 3:
                            heapq.heappushpop(max_heap, (max_ele, i_max))
                            heapq.heappushpop(min_heap, (min_ele, i_min))
                        else:
                            heapq.heappush(max_heap, (max_ele, i_max))
                            heapq.heappush(min_heap, (min_ele, i_min))
            
            if len(max_heap) == 3:
                heapq.heappushpop(max_heap, (-cost[u], u))
                heapq.heappushpop(min_heap, (cost[u], u))
                ans[u] = get_max_mul(min_heap, max_heap)
            else:
                heapq.heappush(max_heap, (-cost[u], u))
                heapq.heappush(min_heap, (cost[u], u))
                if len(max_heap) == 3:
                    ans[u] = get_max_mul(min_heap, max_heap)

            return max_heap, min_heap
        
        dfs(0, -1)
        return ans



