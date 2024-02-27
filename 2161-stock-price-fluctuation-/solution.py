import heapq
class StockPrice:

    def __init__(self):
        self.stocks = {}
        self.max_time = 0

        self.min_price = []
        self.max_price = []

        

    def update(self, timestamp: int, price: int) -> None:
        self.stocks[timestamp] = price 
        if self.max_time < timestamp:
            self.max_time = timestamp
        
        heapq.heappush(self.min_price, (price, timestamp))
        heapq.heappush(self.max_price, (-price, timestamp))


    def current(self) -> int:
        return self.stocks[self.max_time]
        

    def maximum(self) -> int:
        price, timestamp = self.max_price[0]

        while self.stocks[timestamp] != abs(price):
            heapq.heappop(self.max_price)
            price, timestamp = self.max_price[0]
        return abs(price)
        

    def minimum(self) -> int:
        price, timestamp = self.min_price[0]

        while self.stocks[timestamp] != price:
            heapq.heappop(self.min_price)
            price, timestamp = self.min_price[0]
        
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
