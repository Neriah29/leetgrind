class TimeMap:

    def __init__(self):
        """
`       I am thinking that we
        can use an array to store all the values, because we want the order to be preserved
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        """
        Here we are tring to do a binary search for timestamp or the nearest to it that is less 
        than it
        """
        l, r = 0, len(self.store[key]) -1
        result = ""
        #we want to filter through for the key.
        while l <= r:
            m = (r + l) // 2

            if self.store[key][m][0] == timestamp:
                return self.store[key][m][1]
            elif self.store[key][m][0] > timestamp:
                r = m - 1
            else:
                result = self.store[key][m][1]
                l = m + 1
        
        return result
                
        
