"""
we can use a map structure to store the values and timestamps per key
we will us e abinary search to go through valiues of required key 
when geting.
"""

class TimeMap:

    def __init__(self):
        self._valStore = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #adding (val and timestamp) to dict[key]
        self._valStore[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #do a binary search 
        currStore = self._valStore[key]
        l, r = 0, len(currStore) -1
        while l <= r:
            m = (l +r)//2
            if currStore[m][0] <= timestamp:
                res = currStore[m][1]
                l = m+1
            else:
                r = m -1     

        return res

        
