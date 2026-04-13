class StockSpanner:

    def __init__(self):
        self.stocks = []        

    def next(self, price: int) -> int:
        res = 1
        N = len(self.stocks) - 1
        while N >= 0 and self.stocks[N] <= price:
            N -= 1
            res += 1
        self.stocks.append(price)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)