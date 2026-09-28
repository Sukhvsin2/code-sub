# solution works but time complexity is high

class TimeMap:

    def __init__(self):
        self.Keystore = {} # init hashmap
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Keystore:
            self.Keystore[key] = [] # init empty hashmap
        if timestamp not in self.Keystore[key]:
            self.Keystore[key].append((value, timestamp)) # append value in timestamp hashmap
        self.Keystore[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Keystore:
            return ""

        timestamps = self.Keystore[key]

        l, r = 0, len(timestamps)-1

        while l <= r:
            mid = (l+r)//2

            if timestamps[mid][1] == timestamp:
                return timestamps[mid][0]
            
            if timestamps[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if timestamp < timestamps[0][1]:
            return ""
        
        return timestamps[r][0]

        
