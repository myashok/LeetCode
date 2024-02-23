import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for from_city, to_city, price in flights:
            g[from_city].append((to_city, price))
        
        distance = {}
        dist_heap = []
        heapq.heappush(dist_heap, (0, src, k + 1))
        while dist_heap:
            price, city, stop = heapq.heappop(dist_heap)
            if city == dst:
                return price

            if stop:
                for neighbour_city, neighbour_price in g[city]:
                    if distance.get((neighbour_city, stop - 1), math.inf) > price + neighbour_price:
                        distance[(neighbour_city, stop - 1)] = price + neighbour_price
                        heapq.heappush(dist_heap, (price + neighbour_price, neighbour_city, stop - 1))
        return -1
