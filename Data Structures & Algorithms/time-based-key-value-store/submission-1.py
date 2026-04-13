class TimeMap:
    # all history is relevant - one might want to query value at timestamp 1
    # optimization: binary search on timestamps?
    # timestamp could be an additional key within kv
    def __init__(self):
        self.kv = defaultdict(list) # key: list[(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        history = self.kv[key]
        res = ""
        l, r = 0, len(history) - 1
        while l <= r:
            m = (l + r) // 2
            time, value = history[m]
            if time <= timestamp:
                res = value
                l = m + 1
            else:
                r = m - 1
        return res

    def getv2(self, key: str, timestamp: int) -> str:
        history = self.kv[key]
        res = None
        for time, value in history:
            if time > timestamp:
                break
            res = value
        return res
        
