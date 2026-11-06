class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        self.stocks.append(price)
        i = len(self.stocks) - 2
        while i >= 0 and self.stocks[i] <= price:
            i -= 1
        return len(self.stocks) - i - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)