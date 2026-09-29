# solution works better
class TimeMap:

    def __init__(self):
        self.Keystore = {} # init hashmap
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Keystore:
            self.Keystore[key] = [] # init empty hashmap
        self.Keystore[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Keystore:
            return ""

        timestamps = self.Keystore.get(key, [])
        res = ""
        l, r = 0, len(timestamps)-1

        while l <= r:
            mid = (l+r)//2

            if timestamps[mid][1] <= timestamp:
                res = timestamps[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

        
