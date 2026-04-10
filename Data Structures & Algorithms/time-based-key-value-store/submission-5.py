class TimeMap:

    def __init__(self):
        self._val = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._val[key].append((timestamp, value))
        return None

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        curr = self._val[key]
        l, r = 0, len(curr) -1

        while l <= r:
            m = (l+r)//2

            if curr[m][0] <= timestamp:
                res = curr[m][1]
                l = m + 1

            elif curr[m][0] > timestamp:
                r = m -1

            else:
                return curr[m][1]

        return res
