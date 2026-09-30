class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore: 
            return ""

        timestamps = self.keystore.get(key, [])
        l, r = 0, len(timestamps)-1
        res = ""

        while l<=r:
            mid = (l+r) // 2

            if timestamps[mid][0] <= timestamp:
                res = timestamps[mid][1]
                l = mid + 1
            else:
                r = mid -1 

        return res
