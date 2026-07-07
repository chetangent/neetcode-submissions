class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        x = self.d.get(key, [])
        l, h = 0, len(x) - 1
        while l <= h:
            mid = l + (h - l) // 2
            if x[mid][1] <= timestamp:
                res = x[mid][0]
                l = mid + 1
            else:
                h = mid - 1
        return res
