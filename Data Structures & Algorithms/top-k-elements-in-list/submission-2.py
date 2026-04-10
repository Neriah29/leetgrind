class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []
        for n in nums:
            freq[n] += 1
        sortedItems = sorted(freq.items(),key = lambda x : x[1], reverse = True)
        c = 0
        for key, val in sortedItems:
            if c >= k:
                break
            else:
                res.append(key)
            c += 1
        return res
