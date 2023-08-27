# initiate a dictionaries to save key, value
# for setting a value, check if the key is in dict and append key, value, timestamp
# for getting a value, check mid value if less than timestamp
class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


timeMap = TimeMap()
# store the key "foo" and value "bar" along with timestamp = 1.
timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1)         # return "bar"
# return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.get("foo", 3)
# store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4)         # return "bar2"
timeMap.get("foo", 5)
